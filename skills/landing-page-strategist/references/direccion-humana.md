# Dirección humana y ejecución visual

## Entrevistar para encontrar una voz

Integra estas preguntas en los bloques existentes, sin alargar la entrevista con información ya conocida:

- ¿Qué te dicen literalmente tus clientes cuando llegan y qué les preocupa?
- ¿Qué experiencia personal te llevó a ofrecer esto y qué haces de una manera propia?
- ¿Qué momento cotidiano mejora tu producto o servicio? Describe una escena concreta.
- ¿Cómo hablarías con alguien que todavía tiene dudas? ¿Qué expresiones usarías y cuáles nunca?
- ¿Qué personas, lugares, objetos, procesos o detalles reales podemos mostrar?

Recoge frases textuales con su procedencia. No conviertas frases hipotéticas en testimonios. Si no hay material suficiente, propone una voz provisional y pregunta por un ejemplo real; no fabriques una historia del fundador.

## Concepto antes del layout

Define una idea rectora específica del negocio: una tensión humana, una promesa demostrable y una imagen que la haga visible. Explica en tres frases qué queremos que el visitante sienta, entienda y haga. Elige una dirección principal y un contrapunto, no una mezcla de cuatro marcas.

Ejemplo hipotético dental: «Saber qué va a pasar antes de sentarte en el sillón». Puede traducirse en fotos del equipo explicando, una secuencia de primera visita y copy que responda a la incertidumbre. Solo afirmar procedimientos y condiciones confirmados. No reducir el concepto a “premium, moderno y limpio”.

## Transferir las referencias a decisiones

Estas son traducciones creativas del contenido consultado, no afirmaciones de que sus layouts o animaciones sean idénticos a estas propuestas. Consulta las URLs en `referentes.md`; cuando haya navegador, inspecciona también escritorio, móvil y recorrido de scroll antes de atribuir un recurso visual a una fuente. Registra las limitaciones si solo accedes a texto.

| Referente | Patrón observado | Decisión aplicable |
|---|---|---|
| Andrea Badillo | Voz reconocible, presentación personal, programas y testimonios | Hacer visible a la persona detrás de la oferta, conservar lenguaje propio y conectar su experiencia con la necesidad del visitante. Proponer retrato editorial y prueba con contexto, no una biografía genérica. |
| Shopify | Aspiración, capacidades y ejemplos de negocios | Mostrar una tarea concreta y su resultado. Diseñar una demostración o escena de uso en lugar de explicar cada beneficio con un icono dentro de una tarjeta. |
| Apple | Promesa breve, destacados, producto, detalles y comparación | Dar protagonismo al producto y revelar información por niveles. Proponer una escena visual amplia, acercamientos útiles y detalles accesibles sin obligar a consumir toda una animación. |
| Vilma Núñez | Posicionamiento, historia, educación y captación | Construir confianza con experiencia pertinente y una muestra útil del conocimiento. El recurso gratuito debe preparar el siguiente paso, no competir con toda la oferta. |

Por cada patrón elegido, anota en el brief: fuente → necesidad del cliente → sección → recurso visual o interacción → adaptación móvil. No basta con mencionar “inspirado en Apple”.

## Guion con ritmo

Antes de programar, define cada sección con: pregunta del visitante, emoción, mensaje, evidencia, composición, recurso, movimiento y siguiente paso. Alterna momentos de impacto, explicación y prueba. Cada desplazamiento debe aportar algo nuevo.

Para una página larga, utiliza varias familias de composición según el contenido: escena fotográfica amplia, bloque editorial, demostración, galería asimétrica, proceso, comparación o cita contextualizada. Evita tres secciones consecutivas con la misma estructura de título y tarjetas. No alternes izquierda/derecha mecánicamente ni conviertas todo en bento.

Diseña un momento distintivo ligado a la oferta: recorrido visual del servicio, explorador de variantes, demo real, detalle ampliable del producto o historia documentada. No agregues juegos o animaciones solo para mantener atención. Una landing puede ser clara y sofisticada sin ser visualmente recargada.

## Especificación visual con la precisión del prompt dental

Para hero y secciones principales, concreta antes de implementar:

- Grid, proporciones, ancho máximo, posición y escala del texto y de la imagen.
- Tipografía de titulares y cuerpo, pesos, interlineado, ancho de lectura y escala responsive. Verifica que el titular y CTA se entiendan en un portátil pequeño.
- Roles de color y contraste sobre fotografía; fondos y transiciones entre secciones que sirvan a la historia.
- Recurso exacto, procedencia, encuadre, punto focal y tratamiento en móvil. Una imagen genérica no sustituye una demostración del negocio.
- Estados de hover, foco, carga y error; animación con disparador, duración, distancia y alternativa reducida.

El mosaico de imagen compartida del prompt dental es una opción de composición real, no solo una palabra de inspiración. Cuando corresponda, usa una imagen continua con ventanas alineadas: escala `s = max(anchoContenedor/anchoImagen, altoContenedor/altoImagen)`; calcula ancho y alto renderizados; distribuye el exceso según el punto focal; resta el offset de cada ventana respecto al contenedor al establecer su posición de fondo. Recalcula con ResizeObserver y al cargar la imagen. En móvil conserva continuidad solo si el encuadre funciona; de lo contrario usa una imagen completa. Incluye fondo alternativo ante error de carga.

También puedes trasladar del prompt el contraste entre una composición fotográfica y un bloque editorial, la jerarquía tipográfica fuerte y revelados escalonados. No heredes el splash artificial, alturas que recorten texto o tarjetas anidadas sin función.

## Copy que suena a una persona

Escribe desde situaciones observables y decisiones reales. Sustituye “soluciones innovadoras para transformar tu vida” por una explicación concreta de qué se hace, para quién y cómo ayuda. Evita “lleva al siguiente nivel”, “experiencia única”, “calidad excepcional” y superlativos sin evidencia.

Lee el copy en voz alta. Varía longitud y cadencia; elimina frases que nadie diría en una conversación. Mantén el tratamiento del público y su vocabulario. Cercanía no significa imponer jerga, diminutivos o emojis. No explotes inseguridades ni exageres dolor para fabricar urgencia.

Prueba de sustitución: si cambiar el nombre y la foto permite usar el hero en cinco negocios distintos, reescríbelo. Los beneficios deben contener información propia del cliente. El CTA debe explicar el compromiso real y qué sucede después.

## Movimiento con propósito

Planifica una entrada principal y transiciones que guíen atención, además de feedback en controles. Usa transform y opacity cuando basten; evita mover todas las secciones del mismo modo. Como punto de partida, microinteracciones de 150–250 ms y entradas de 400–700 ms, ajustadas al contenido. El hero no debe esperar un loader para mostrarse.

Respeta reduced-motion, teclado y navegación táctil. Todo contenido y acción deben seguir disponibles sin animación. Reserva scroll vinculado, pinning o zoom para demostraciones donde expliquen algo; ofrece una composición móvil que no dependa de esos efectos. No bloquees el scroll normal para forzar la narrativa.

## Revisión visual obligatoria

Después del build, abre la página y revisa capturas de hero, una sección central y cierre en escritorio y móvil. Compara la implementación con el guion y corrige problemas observados antes de entregar. Si no hay navegador disponible, declara la revisión visual pendiente; un build correcto no la reemplaza.

Evalúa con evidencia visible:

1. Identidad: ¿hay una idea y recursos propios del negocio o solo cambios de color?
2. Voz: ¿el texto contiene lenguaje y situaciones del cliente?
3. Ritmo: ¿cada sección aporta información nueva y evita repetición mecánica?
4. Demostración: ¿se ve el producto, servicio o proceso real?
5. Jerarquía: ¿oferta y CTA se entienden sin competir con decoración?
6. Ejecución: ¿encuadres, espaciado, tipografía y movimiento funcionan en móvil?

Si falla alguno, corrige la causa concreta. No asignes una puntuación “premium” sin evidencia. Entrega una breve explicación del concepto, los patrones adaptados y las comprobaciones realizadas. La calidad final debe evaluarse sobre páginas construidas, no solo sobre esta documentación.
