# Plan de Diseño Inicial - Arquitectura del Juego

Este documento describe la arquitectura inicial propuesta para el juego, centrada en las clases fundamentales: `Pelota`, `Campo` y `Juego`.

## Clases Fundamentales

### 1. Clase `Pelota`

*   **Rol Principal:** Representa un objeto móvil dentro del juego que se desplaza y potencialmente interactúa con el entorno y otras pelotas.
*   **Atributos Clave:**
    *   `posicion` (Vector): Vector de 2 dimensiones que indica la ubicación actual del centro de la pelota.
    *   `velocidad` (Vector): Vector de 2 dimensiones que indica la dirección y magnitud del movimiento por unidad de tiempo.
    *   `radio` (Flotante): El radio de la pelota, usado para detección de colisiones y renderizado.
    *   `color` (Tupla/Color): El color con el que se dibujará la pelota.
*   **Interacciones:**
    *   Su estado (`posicion`, `velocidad`) es actualizado por la clase `Juego` en cada iteración del bucle principal.
    *   Interactúa con el `Campo` (verificación de límites/colisiones con bordes).
    *   Potencialmente interactuará con otras instancias de `Pelota` (colisiones entre pelotas).

### 2. Clase `Campo`

*   **Rol Principal:** Define los límites y propiedades del área de juego. Actúa como el contenedor para los objetos móviles.
*   **Atributos Clave:**
    *   `ancho` (Entero): La dimensión horizontal del campo.
    *   `alto` (Entero): La dimensión vertical del campo.
    *   `limites` (Rectángulo/Tupla): Representación de los bordes del campo (ej. (0, 0, ancho, alto)).
*   **Interacciones:**
    *   Proporciona la información necesaria para que la clase `Juego` verifique si una `Pelota` ha chocado con un borde.
    *   No tiene comportamiento activo; es principalmente una estructura de datos y límites.

### 3. Clase `Juego`

*   **Rol Principal:** Es el controlador central del juego. Gestiona el bucle principal, actualiza el estado de todos los objetos, maneja la lógica del juego (movimiento, colisiones) y coordina la renderización.
*   **Atributos Clave:**
    *   `campo` (Instancia de `Campo`): Referencia al área de juego.
    *   `pelotas` (Lista de instancias de `Pelota`): Colección de todas las pelotas activas en el juego.
    *   `estado_juego` (Enumeración/Cadena): Representa el estado actual del juego (ej. 'corriendo', 'pausado', 'terminado').
    *   `pantalla` (Objeto de renderizado): Referencia a la superficie donde se dibujará el juego (si aplica, ej. `pygame.Surface`).
*   **Interacciones:**
    *   Itera sobre la lista de `pelotas` para actualizar su posición basándose en su velocidad y el tiempo transcurrido.
    *   Verifica colisiones de cada `pelota` con los `limites` del `campo` y ajusta la velocidad en consecuencia (rebote).
    *   Maneja el bucle principal del juego (actualizar -> dibujar).
    *   Podría manejar la creación y eliminación de `pelotas`.
    *   Coordina la llamada a los métodos de dibujo de las `pelotas` y el `campo`.

## Decisiones de Diseño Iniciales

*   **Uso de Vectores:** Se decidió utilizar objetos vectoriales (ej. `pygame.math.Vector2` si se usa Pygame) para representar `posicion` y `velocidad`. Esto simplifica enormemente las operaciones de movimiento (posición + velocidad * tiempo) y las operaciones de colisión/rebote (reflexión vectorial).
*   **Simulación de Física Simple:** Inicialmente, la simulación de movimiento se basará en una integración de Euler simple: `nueva_posicion = posicion_actual + velocidad * delta_tiempo`. El manejo de colisiones con los bordes será una simple inversión del componente de velocidad relevante (ej. `velocidad.x *= -1` para un rebote horizontal).
*   **Responsabilidad Centralizada:** La lógica principal del juego (actualización de estado, detección y respuesta a colisiones con bordes) reside en la clase `Juego`. Las clases `Pelota` y `Campo` son principalmente contenedores de datos y propiedades.

## Resumen de Investigación (Paso 1)

La investigación inicial se centró en los fundamentos de la simulación de movimiento simple en 2D y la detección de colisiones básicas. Se revisaron conceptos como:

*   **Bucle de Juego:** La estructura estándar (procesar entrada -> actualizar estado -> dibujar).
*   **Integración Numérica:** Métodos básicos para actualizar la posición de un objeto en movimiento (Euler simple es suficiente para empezar).
*   **Detección de Colisiones:** Conceptos como AABB (Axis-Aligned Bounding Box) y detección círculo-rectángulo/círculo-punto para verificar si una pelota toca un borde rectangular.
*   **Respuesta a Colisiones:** Cómo modificar la velocidad de un objeto para simular un rebote contra una superficie.

Estos hallazgos informaron la decisión de usar vectores y centralizar la lógica de actualización y colisión en la clase `Juego`.