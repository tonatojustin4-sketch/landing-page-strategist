# Instalación y actualización

## Opción 1: copiar y pegar en Codex

```text
$skill-installer instala https://github.com/tonatojustin4-sketch/landing-page-strategist/tree/main/skills/landing-page-strategist
```

Para una versión fija, cambia `main` por `v1.0.0`. El instalador integrado determina la ubicación en tu entorno; en la versión usada para verificar este repositorio es `$CODEX_HOME/skills`, o `~/.codex/skills` si no está definida esa variable. La documentación actual también describe `~/.agents/skills` como ubicación de skills personales. Evita instalar dos copias con el mismo nombre en rutas diferentes.

La skill estará disponible en el siguiente turno. Si no aparece, reinicia Codex. Consulta la [documentación oficial](https://developers.openai.com/codex/skills/) para las ubicaciones que admite tu versión.

## Opción 2: instalador Python independiente

Requiere Python 3.10 o superior y acceso HTTPS a GitHub al descargar. No necesita paquetes adicionales. Descarga el instalador de una versión fija:

```bash
curl --fail --location --output install-landing-page.py https://raw.githubusercontent.com/tonatojustin4-sketch/landing-page-strategist/v1.0.0/install.py
```

Puedes revisar ese archivo antes de ejecutarlo. Después:

```bash
python3 install-landing-page.py
```

Descarga `v1.0.0` y copia únicamente la skill en `~/.agents/skills/landing-page-strategist`, una ubicación personal descrita en la documentación oficial. No modifica configuración, no solicita credenciales y no sobrescribe instalaciones existentes.

Para usar otra carpeta, por ejemplo la ubicación del instalador integrado:

```bash
python3 install-landing-page.py --dest ~/.codex/skills
```

Para inspeccionar el destino sin descargar ni escribir:

```bash
python3 install-landing-page.py --dry-run
```

Si lo ejecutas desde un clon completo de este repositorio, instala la copia local incluida junto al script. Fuera del repositorio descarga la versión fija. Para cambiar la referencia de descarga:

```bash
python3 install-landing-page.py --ref main
```

`main` puede cambiar con el tiempo; el tag fija esta primera publicación. El instalador utiliza únicamente la biblioteca estándar de Python.

## Opción 3: desde un clon

```bash
git clone https://github.com/tonatojustin4-sketch/landing-page-strategist.git
cd landing-page-strategist
python3 install.py
```

Para uso exclusivo de un proyecto, copia la carpeta `skills/landing-page-strategist` completa a `.agents/skills/landing-page-strategist` dentro de ese proyecto. No copies todo el repositorio a la carpeta de skills.

## Actualizar

El instalador se detiene si encuentra el destino ocupado, incluso si es un enlace simbólico. Antes de actualizar, mueve la carpeta instalada a un respaldo fuera de las carpetas que Codex escanea para skills. Luego instala la nueva versión. Conserva tus cambios locales antes de sustituirla. No hay actualización automática ni borrado automático.

## Desinstalar

Retira la carpeta `landing-page-strategist` de la ruta donde la instalaste. Esto no elimina las páginas web que hayas construido con ella. Si quieres conservar la skill sin que aparezca, mueve la carpeta fuera de las rutas de descubrimiento o usa la configuración de desactivación de tu versión de Codex.

## Solución de problemas

| Síntoma | Qué revisar |
|---|---|
| El instalador indica que ya existe | Localiza y respalda esa instalación antes de actualizar. |
| No aparece la skill | Comprueba que la carpeta contiene `SKILL.md`, revisa su ubicación y reinicia Codex. |
| Aparece duplicada | Revisa instalaciones en rutas personales y `.agents/skills` del proyecto. |
| Falla la descarga | Comprueba red, proxy, permisos y existencia de la referencia en GitHub. El instalador independiente está pensado para este repositorio público. |
| Python no existe o es antiguo | Usa Python 3.10+ o pide a Codex usar `$skill-installer`. |
| Solo recibes una estrategia | Pide la implementación completa y confirma que el entorno dispone del proyecto y herramientas para construir. |

## Verificar el repositorio antes de publicar cambios

```bash
python3 -m unittest discover -s tests -v
ruby scripts/validate.rb
```

La validación de Ruby requiere Ruby con su biblioteca YAML estándar. Comprueba metadatos y enlaces locales; las pruebas de Python verifican el instalador. Estas comprobaciones no sustituyen una evaluación real de la calidad de las páginas generadas.
