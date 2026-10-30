# Landing Page Strategist

**De una entrevista con el cliente a una landing page funcional, editable y preparada para entregar.**

Skill en español para Codex. Reúne descubrimiento comercial, arquitectura de conversión, copy, diseño responsive, desarrollo y verificación en un mismo flujo. Está pensada para productos, servicios, formación, SaaS y marcas personales, incluyendo profesionales que construyen páginas para sus clientes.

## Instalación rápida en Codex

Copia y pega este mensaje en un chat de Codex con acceso a archivos y red:

```text
$skill-installer instala esta skill desde https://github.com/tonatojustin4-sketch/landing-page-strategist/tree/main/skills/landing-page-strategist
```

El enlace identifica la carpeta completa de la skill, incluyendo sus referencias. No basta con copiar únicamente `SKILL.md`. Pegar un enlace no ejecuta una instalación por sí mismo: la instrucción pide al instalador de Codex que la realice, sujeto a los permisos del entorno.

También puedes usar la [versión fija v1.1.0](https://github.com/tonatojustin4-sketch/landing-page-strategist/tree/v1.1.0/skills/landing-page-strategist) en lugar de `main`.

Para instalar desde terminal, usar el instalador independiente o actualizar una versión, consulta [INSTALL.md](INSTALL.md).

## Empezar

Después de instalarla, envía en el siguiente turno:

```text
Usa $landing-page-strategist. Quiero crear una landing para un cliente
que ofrece servicios de odontología en Quito. El objetivo es conseguir
reservas por WhatsApp. Entrevístame y construye el proyecto completo.
```

Puedes seleccionar la skill desde el selector de tu aplicación. Si no aparece después de instalarla, reinicia Codex. La forma de invocarla puede variar según la interfaz; la documentación oficial explica [cómo usar skills](https://developers.openai.com/codex/skills/).

## Dirección creativa en v1.1.0

Esta versión exige voz del cliente, concepto específico, guion visual por sección, transferencia explícita de referencias y revisión de capturas. Incluye especificación del mosaico del prompt dental, ritmo editorial y movimiento con propósito. Consulta [dirección humana](skills/landing-page-strategist/references/direccion-humana.md).

## Cómo funciona

1. **Entrevista por bloques.** Pregunta por oferta, audiencia, objetivo, evidencia, marca, recursos y funcionamiento, sin repetir lo que ya sabe.
2. **Estrategia.** Define propuesta de valor, acción principal, objeciones y estructura adecuada al tipo de compra.
3. **Copy y diseño.** Escribe contenido específico y desarrolla una dirección visual coherente con la marca.
4. **Construcción.** Implementa el proyecto completo. Conserva el stack existente; para proyectos nuevos sin restricciones parte de React + Vite + TypeScript.
5. **Verificación.** Revisa build, móvil, escritorio, navegación y recorrido de conversión en los entornos disponibles.
6. **Entrega.** Proporciona código editable, instrucciones de ejecución y despliegue, guía de personalización e inventario de recursos.

La implementación es el resultado por defecto. Si solicitas expresamente solo estrategia o un prompt para otra herramienta, adapta la entrega a ese alcance.

## Qué puedes recibir

- Brief comercial y mapa de secciones.
- Textos y diseño adaptados al negocio.
- Proyecto web con código fuente y recursos.
- WhatsApp, agenda, formulario o checkout según el alcance y los servicios disponibles.
- Instrucciones para modificar, ejecutar y desplegar.
- Registro de verificaciones y dependencias pendientes.

**Preparada para desplegar** significa que el proyecto está construido, documentado y comprobado en el entorno disponible. **Operativa en producción** requiere publicación y verificación del recorrido principal en el entorno final. La skill debe informar cuál es el estado real.

## Qué necesita

- Un entorno de Codex capaz de leer y escribir el proyecto y ejecutar comandos para construirlo.
- Acceso a navegador para la revisión visual, cuando esté disponible.
- Datos reales del negocio y recursos con permisos adecuados.
- Acceso autorizado a los servicios que necesite la integración elegida.

La skill es un paquete de instrucciones: no incluye un hosting, una cuenta de pagos ni un servicio de formularios. Instalarla no instala React ni publica una página; esas acciones ocurren durante cada proyecto según su alcance. No requiere una API key adicional para leer sus instrucciones; servicios externos pueden tener requisitos y costes propios.

## Referentes y criterio

Toma patrones de comunicación de Andrea Badillo, Shopify, Apple y Vilma Núñez: marca personal, demostración, beneficios, autoridad y captación. También transforma un prompt visual dental en un proceso adaptable a otras ofertas. No copia sus imágenes, identidad o textos ni presupone sus tasas de conversión.

Consulta el [análisis y sus límites](skills/landing-page-strategist/references/referentes.md).

## Documentación

- [Instalación y actualización](INSTALL.md).
- [Ejemplos, flujo y alcance](docs/USO.md).
- [Instrucciones de la skill](skills/landing-page-strategist/SKILL.md).
- [Entrevista](skills/landing-page-strategist/references/entrevista.md).
- [Arquitectura y aceptación](skills/landing-page-strategist/references/arquitectura.md).
- [Entrega comercial](skills/landing-page-strategist/references/entrega-comercial.md).

## Límites

La skill no garantiza ventas, testimonios, resultados de negocio ni permisos sobre recursos de terceros. No debe inventar evidencia ni presentar integraciones simuladas como funcionales. Publicar, contratar servicios o transferir cuentas requiere que forme parte del encargo autorizado.

Los proyectos generados pueden destinarse a uso comercial o entregarse a clientes, sujeto a las condiciones aplicables del entorno y las licencias de sus recursos y dependencias. La publicación de este repositorio no acredita exclusividad ni cambia esas condiciones.
