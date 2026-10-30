#!/usr/bin/env python3
"""Install the local skill, or download its fixed release. Python 3.10+."""

from __future__ import annotations

import argparse
import io
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
from urllib.parse import quote
from urllib.request import Request, urlopen
import zipfile

SKILL_NAME = "landing-page-strategist"
REPOSITORY = "tonatojustin4-sketch/landing-page-strategist"
DEFAULT_REF = "v1.0.0"
MAX_ARCHIVE_BYTES = 10 * 1024 * 1024


def validate_source(source: Path) -> None:
    if source.is_symlink() or not source.is_dir():
        raise ValueError("La fuente debe ser una carpeta real de la skill.")
    for entry in source.rglob("*"):
        if entry.is_symlink() or not (entry.is_file() or entry.is_dir()):
            raise ValueError(f"Recurso no permitido: {entry.name}")
    skill_file = source / "SKILL.md"
    if not skill_file.is_file():
        raise ValueError("La fuente no contiene SKILL.md.")
    content = skill_file.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not frontmatter or not re.search(
        rf"^name:\s*{re.escape(SKILL_NAME)}\s*$", frontmatter[1], re.M
    ):
        raise ValueError("La identidad de la skill no coincide.")
    for relative in re.findall(r"\]\((references/[^)]+)\)", content):
        linked = (source / relative).resolve()
        if not linked.is_relative_to(source.resolve()) or not linked.is_file():
            raise ValueError(f"Referencia inválida o ausente: {relative}")


def install_skill(source: Path, destination_root: Path) -> Path:
    validate_source(source)
    target = destination_root.expanduser() / SKILL_NAME
    if os.path.lexists(target):
        raise FileExistsError(f"El destino ya existe; no se sobrescribe: {target}")
    destination_root = target.parent
    if destination_root.resolve().is_relative_to(source.resolve()):
        raise ValueError("El destino no puede estar dentro de la fuente.")
    destination_root.mkdir(parents=True, exist_ok=True)
    # Exclusive directory creation prevents accidental replacement of an existing install.
    target.mkdir()
    try:
        shutil.copytree(source, target, dirs_exist_ok=True)
    except BaseException:
        shutil.rmtree(target)
        raise
    return target


def extract_skill(payload: bytes, destination: Path) -> Path:
    """Extract only skill files, rejecting traversal, symlinks and oversized data."""
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        items = archive.infolist()
        if not items:
            raise ValueError("El archivo descargado está vacío.")
        roots = {PurePosixPath(item.filename).parts[0] for item in items if item.filename}
        if len(roots) != 1:
            raise ValueError("Estructura de descarga inesperada.")
        root = next(iter(roots))
        prefix = (root, "skills", SKILL_NAME)
        selected = []
        size = 0
        for item in items:
            path = PurePosixPath(item.filename)
            if path.is_absolute() or ".." in path.parts or "\\" in item.filename:
                raise ValueError("Ruta no permitida en la descarga.")
            if path.parts[:3] != prefix:
                continue
            mode = (item.external_attr >> 16) & 0o170000
            if mode not in (0, 0o100000, 0o040000):
                raise ValueError("Enlaces y archivos especiales no permitidos.")
            size += item.file_size
            if size > MAX_ARCHIVE_BYTES:
                raise ValueError("La skill supera el tamaño de descarga permitido.")
            selected.append((item, path.parts[3:]))
        source = destination / SKILL_NAME
        source.mkdir()
        for item, relative in selected:
            output = source.joinpath(*relative)
            if item.is_dir():
                output.mkdir(parents=True, exist_ok=True)
            else:
                output.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(item) as reader, output.open("xb") as writer:
                    shutil.copyfileobj(reader, writer)
    validate_source(source)
    return source


def download_skill(ref: str, destination: Path) -> Path:
    if not ref or ref.startswith("-") or any(char.isspace() for char in ref):
        raise ValueError("Referencia de GitHub no válida.")
    url = f"https://codeload.github.com/{REPOSITORY}/zip/{quote(ref, safe='')}"
    request = Request(url, headers={"User-Agent": "landing-page-strategist-installer/1.0.0"})
    with urlopen(request, timeout=45) as response:
        payload = response.read(MAX_ARCHIVE_BYTES + 1)
    if len(payload) > MAX_ARCHIVE_BYTES:
        raise ValueError("La descarga supera el tamaño permitido.")
    return extract_skill(payload, destination)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills",
                        help="Carpeta de skills de destino (predeterminada: ~/.agents/skills)")
    parser.add_argument("--ref", default=DEFAULT_REF, help="Referencia de descarga si no hay copia local")
    parser.add_argument("--dry-run", action="store_true", help="Mostrar origen y destino sin descargar ni escribir")
    args = parser.parse_args(argv)
    local = Path(__file__).resolve().parent / "skills" / SKILL_NAME
    target = args.dest.expanduser() / SKILL_NAME
    print(f"Origen: {local if local.is_dir() else REPOSITORY + '@' + args.ref}")
    print(f"Destino: {target}")
    if args.dry_run:
        print("Simulación: no se ha descargado ni escrito ningún archivo.")
        return 0
    try:
        if os.path.lexists(target):
            raise FileExistsError(f"El destino ya existe; no se sobrescribe: {target}")
        if local.is_dir():
            installed = install_skill(local, args.dest)
        else:
            with tempfile.TemporaryDirectory(prefix="landing-skill-") as temporary:
                source = download_skill(args.ref, Path(temporary))
                installed = install_skill(source, args.dest)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"No se pudo instalar: {error}", file=sys.stderr)
        return 1
    print(f"Skill instalada en {installed}")
    print("Disponible en el siguiente turno de Codex. Si no aparece, reinicia Codex.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
