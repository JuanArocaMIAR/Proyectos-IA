Descripción del Proyecto:
Este proyecto tiene como objetivo desarrollar un sistema que detecte y cuente coches en videos en tiempo real utilizando el modelo YOLOv5 para la detección de objetos y OpenCV para el procesamiento de video. El sistema puede identificar coches, asignarles un ID único y llevar un registro de cuántos vehículos han pasado por una zona definida dentro del video.

Funcionalidades:
Detección de vehículos: Utiliza el modelo YOLOv5 para detectar coches en cada fotograma del video.
Conteo en tiempo real: Cuenta cuántos coches cruzan una zona de interés, definida dentro del video.
Seguimiento único: A cada coche detectado se le asigna un ID único para evitar conteos duplicados.
Visualización: Se muestran el video procesado con las cajas delimitadoras y el conteo total de vehículos detectados en pantalla.

Pipeline del Proyecto:
Procesamiento del Video: Se utiliza OpenCV para capturar el video y procesar cada fotograma.
Detección con YOLOv5: YOLOv5 detecta los coches y marca sus posiciones con cajas delimitadoras.
Definición de Zona de Conteo: Se define una región del video en la que el sistema cuenta los coches que la cruzan.
Conteo y Seguimiento: Los vehículos son rastreados para evitar múltiples conteos de un mismo coche.
Salida Visual: El sistema muestra el número de coches que han cruzado la zona de conteo en tiempo real.

Requisitos del Sistema:
Python 3.x
YOLOv5 (instalación desde el repositorio oficial de YOLO)
OpenCV
Torch (para la ejecución de modelos YOLO)

Resultados Esperados:
Detección precisa de coches en tiempo real.
Conteo exacto de vehículos que cruzan la zona definida.
Visualización clara del video con las cajas delimitadoras alrededor de los coches.

Para cualquier pregunta o colaboración, no dudes en contactarme a través de juan.arocap@outlook.es o en https://www.linkedin.com/in/juan-aroca-perez/.
Si te interesa colaborar, ¡toda contribución es bienvenida!