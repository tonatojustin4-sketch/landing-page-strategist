# Implementación y entrega comercial

## Resultado esperado

Construye un proyecto que el usuario pueda ejecutar, modificar y entregar o vender a su cliente. Esto requiere diseño y copy específicos, código fuente completo, funcionamiento verificable y documentación de entrega. No garantiza ventas ni acredita por sí solo derechos exclusivos sobre todos los recursos.

## Construcción

1. Inspecciona el proyecto y sus instrucciones. Reutiliza el stack existente; para un proyecto nuevo sin restricciones usa React + Vite + TypeScript como base. Elige dependencias justificadas y versiones compatibles disponibles en el entorno.
2. Implementa el contenido y la dirección visual del brief. Organiza componentes y estilos para permitir mantenimiento; no concentres toda la página en un archivo por herencia del ejemplo dental.
3. Centraliza los datos que el cliente editará con frecuencia: textos, oferta, precios confirmados, enlaces, contacto y recursos. Define colores y tipografía mediante tokens. No conviertas esto en un constructor complejo si el alcance es una landing.
4. Construye el recorrido de conversión completo acordado. Un enlace real a WhatsApp, agenda o checkout existente puede resolverlo sin backend propio. Si se requiere formulario, conecta un receptor real dentro del alcance y configura sus estados; no sustituyas la recepción por una alerta o un éxito simulado.
5. Incluye los archivos de configuración necesarios, scripts de ejecución y build, archivo de dependencias bloqueadas según el gestor y recursos referenciados correctamente. Si hay variables, entrega `.env.example` con nombres y valores de muestra seguros; nunca credenciales reales en el frontend ni en el paquete de entrega.

## Recursos para uso comercial

Usa imágenes, fuentes, iconos y dependencias con permisos compatibles con el uso previsto. Registra procedencia, licencia conocida, atribución y restricciones relevantes en un inventario de recursos. No asumas que una imagen encontrada en internet puede revenderse ni reutilices imágenes de las referencias como material del cliente.

Para recursos aportados por el cliente, registra esa procedencia y cualquier autorización declarada sin presentarla como verificación independiente. Si los derechos son desconocidos, reemplaza el recurso o identifica el pendiente antes de declarar la entrega comercial completa. Los enlaces de inspiración no otorgan derechos de copia. No prometas exclusividad sobre recursos de stock, fuentes o dependencias de terceros.

## Verificación de la entrega

Aplica los criterios de `arquitectura.md` y además:

- Instala o utiliza dependencias según el entorno y ejecuta el build de producción. Corrige los errores dentro del alcance.
- Abre la página en un navegador cuando sea posible y revisa visualmente móvil y escritorio. Comprueba legibilidad, composición, recursos, menú y acción principal; corrige lo observado.
- Recorre la conversión de extremo a extremo en un entorno de prueba adecuado cuando esté disponible. No ejecutes cargos reales ni envíes mensajes a terceros sin autorización. Distingue la validación local de la confirmación de recepción externa.
- Comprueba que las instrucciones correspondan a los comandos y archivos reales del proyecto. No inventes resultados de pruebas o despliegues.
- Si alguna comprobación no se puede hacer, explica cuál y qué falta. Entrega lo completado sin confundirlo con un sistema ya verificado en producción.

## Paquete de entrega

Incluye en el proyecto una guía de entrega breve que indique:

- Cómo instalar, ejecutar, generar el build y previsualizarlo, con comandos reales.
- Dónde cambiar textos, colores, imágenes, precios y datos de contacto.
- Cómo configurar formularios, reservas, pagos o servicios contratados; cuentas, costes recurrentes y titularidad pendientes cuando se conozcan.
- Cómo desplegar según el hosting elegido y configurar dominio y variables cuando corresponda. Si aún no hay hosting, documenta la salida de build y una ruta compatible sin afirmar que ya está publicada.
- Inventario de recursos y atribuciones que deben conservarse.
- Qué se verificó, qué está conectado y qué necesita completar el propietario antes de publicar o captar clientes.

Entrega una vista previa accesible si el entorno lo permite y la ubicación del código fuente. Empaqueta un archivo comprimido solo si facilita la entrega o el usuario lo solicita. Publica o transfiere cuentas únicamente cuando forme parte del encargo autorizado.

## Criterio de finalización

La entrega está preparada para desplegar cuando el proyecto compila, la interfaz se ha comprobado en los entornos disponibles, el recorrido principal está implementado y los recursos y la configuración están documentados. Para declararla operativa en producción, además debe estar desplegada y verificarse la conversión principal en el entorno final. Si falta una condición, describe el estado concreto y continúa con el trabajo independiente que sí puedas completar.
