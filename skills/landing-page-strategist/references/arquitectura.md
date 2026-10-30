# Arquitectura, prompt y aceptación

## Selecciona la historia de venta

La secuencia base es una hipótesis editable: promesa → confianza → explicación → demostración → oferta → objeciones → acción. No impongas un número de secciones.

| Bloque posible | Pregunta que responde | Cuándo incluirlo |
|---|---|---|
| Hero | ¿Qué es, para quién y qué hago ahora? | Siempre; titular específico, apoyo breve, CTA y visual relevante. |
| Prueba temprana | ¿Puedo confiar? | Si existen reseñas, credenciales o evidencia pertinente. |
| Problema o aspiración | ¿Esto tiene que ver conmigo? | Si el visitante necesita reconocer su situación. |
| Solución y beneficios | ¿Qué cambia y cómo? | Vincula beneficios a mecanismos reales, sin promesas genéricas. |
| Demo, galería o casos | ¿Cómo se ve o qué evidencia existe? | Cuando mostrar sea más convincente que describir. |
| Proceso | ¿Qué pasará después? | Reservas, servicios, incorporaciones y compras complejas. |
| Oferta y precio | ¿Qué recibo y cuánto cuesta? | Si hay datos confirmados; explica condiciones relevantes. |
| Persona o equipo | ¿Quién responde por esto? | Si la relación o experiencia influye en la compra. |
| Comparación | ¿Por qué esta alternativa? | Si hay diferencias útiles y verificables. |
| FAQ | ¿Qué duda me impide actuar? | Solo objeciones reales, sin repetir toda la página. |
| Cierre | ¿Cuál es mi siguiente paso? | Recapitula valor y presenta la acción principal. |
| Footer | ¿Cómo contacto y consulto condiciones? | Información real y enlaces existentes. |

Para cada sección registra objetivo, mensaje, evidencia, contenido, tratamiento visual y CTA si corresponde. No llenes toda la página de botones ni enlaces que desvíen la compra.

## Adaptación por tipo de oferta

- Producto: protagonismo del producto → demostración → beneficios → detalles para decidir → compra.
- Servicio: resultado buscado → experiencia verificable → alcance y proceso → dudas → reserva o solicitud.
- Formación: transformación de aprendizaje → método y contenidos → instructor y evidencia → condiciones → inscripción.
- SaaS: caso de uso → interfaz y funcionamiento → capacidades relevantes → prueba/casos → planes o demo.
- Marca personal: posicionamiento → autoridad pertinente → oferta principal → prueba → contacto o compra. Si el objetivo es captar suscriptores, el recurso gratuito debe conectar con esa oferta.

Una home con múltiples públicos puede orientar hacia varias páginas. Una landing de campaña suele beneficiarse de un solo objetivo y menos navegación. No copies el megamenú de una plataforma a una campaña local.

## Prompt autosuficiente de implementación

Si este es el entregable solicitado, escríbelo con los siguientes contenidos completos, adaptados al brief:

1. Rol y encargo: construir una landing para el negocio identificado y la oferta concreta.
2. Público, contexto del tráfico y conversión principal con destino real del CTA.
3. Hechos del negocio, oferta, precios y condiciones confirmados; separar supuestos y ausencias.
4. Arquitectura ordenada con propósito y copy de cada sección.
5. Dirección visual: tokens de color, tipografía, ritmo, imágenes y comportamiento móvil.
6. Recursos disponibles y su procedencia; prohibición de fabricar prueba social.
7. Stack, estructura de proyecto e integraciones requeridas, distinguiendo lo disponible de lo pendiente.
8. Estados de interacción y criterios verificables de aceptación.
9. Entregables y límites: qué construir, qué validar y qué no puede declararse operativo todavía.

Si los datos no alcanzan, el prompt debe ordenar preguntar lo imprescindible antes de implementar. No rellenes huecos comerciales con datos de ejemplo que parezcan verdaderos.

## Verificación proporcional

- Mensaje: el primer bloque permite entender oferta, destinatario y siguiente paso; títulos claros y sin afirmaciones sin sustento.
- Responsive: revisar móvil de 360–390 px, tablet y escritorio, además de una altura de portátil; sin scroll horizontal, texto cortado ni CTAs tapados. Dejar crecer el contenido en vez de forzar `h-screen`.
- Accesibilidad: HTML semántico, jerarquía de títulos, labels, texto alternativo útil, teclado, foco visible, menú accesible y contraste adecuado. Respetar `prefers-reduced-motion`.
- Interacción: enlaces y anclas válidos, destinos correctos, menú que cierra correctamente, validación de formulario y estados de carga/error/éxito reales. No usar `href="#"` como acción final.
- Integraciones: probar el recorrido disponible hasta su resultado verificable; declarar lo que no se pudo comprobar. Un botón de pago no demuestra que el checkout esté integrado.
- Rendimiento: imágenes dimensionadas y optimizadas, carga diferida fuera del primer bloque, evitar retrasar el hero; animación ligera. Medir cuando haya entorno disponible, sin inventar puntuaciones.
- SEO: título y descripción específicos, idioma, contenido indexable y datos estructurados solo si corresponden a hechos reales. La URL canónica requiere un dominio final conocido.
- Proyecto: ejecutar build y comprobaciones existentes pertinentes; no introducir dependencias grandes para efectos triviales.
- Medición: proponer eventos como CTA, envío confirmado o compra confirmada según objetivo; no confundir clic con lead o venta. Configurar herramientas solo dentro del alcance autorizado.

Entrega un registro breve de comprobaciones, limitaciones y datos pendientes. Las pruebas A/B deben tener hipótesis, variante y métrica; no afirmar un aumento de conversión antes del experimento.
