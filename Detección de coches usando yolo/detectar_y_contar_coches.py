
import cv2
import numpy as np
import torch
from sort.sort import Sort
import matplotlib.path as mplPath

# Definir la zona de detección
zona_deteccion = np.array([
    [331, 372],
    [414, 479],
    [452, 556],
    [1250, 533],
    [1024, 406],
    [885, 336],
])

def cargar_modelo():
    # Cargar el modelo YOLOv5
    modelo = torch.hub.load('ultralytics/yolov5', model='yolov5s', pretrained=True)
    return modelo

def calcular_centros(bbox):
    # Calcular el centro del bbox
    centro = ((bbox[0] + bbox[2]) // 2, (bbox[1] + bbox[3]) // 2)
    return centro

def obtener_bboxes(predicciones):
    # Obtener las cajas delimitadoras con confianza >= 0.6
    df = predicciones.pandas().xyxy[0]
    df = df[df['confidence'] >= 0.6]
    df = df[df['name'] == 'car']  # Filtrar solo detección de coches
    return df[['xmin', 'ymin', 'xmax', 'ymax']].values.astype(int)

def validar_deteccion(xc, yc):
    # Verificar si el punto (xc, yc) está dentro de la zona definida
    return mplPath.Path(zona_deteccion).contains_points([(xc, yc)])[0]

def procesar_video(cap):
    modelo = cargar_modelo()
    rastreador = Sort(max_age=15, min_hits=5, iou_threshold=0.3)
    coches_detectados_totalmente = set()  # Usamos un conjunto para mantener identificadores únicos

    while cap.isOpened():
        status, frame = cap.read()
        if not status:
            break

        # Detectar coches en el frame
        predicciones = modelo(frame)
        bboxes = obtener_bboxes(predicciones)

        # Dibujar la zona de detección en el frame
        cv2.polylines(frame, [zona_deteccion], isClosed=True, color=(0, 255, 255), thickness=2)

        # Actualizar el rastreador con las nuevas detecciones
        objetos_rastreado = rastreador.update(bboxes)

        detecciones_en_zona = 0  # Contador de coches dentro de la zona
        for obj in objetos_rastreado:
            x1, y1, x2, y2, id_objeto = obj
            xcentro, ycentro = calcular_centros([x1, y1, x2, y2])

            # Almacenar identificadores únicos de coches detectados
            coches_detectados_totalmente.add(int(id_objeto))

            if validar_deteccion(xcentro, ycentro):
                detecciones_en_zona += 1

            # Dibujar la caja delimitadora en el frame
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f'ID: {int(id_objeto)}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # Mostrar las detecciones en la zona en el frame
        cv2.putText(frame, f'Coches en la zona: {detecciones_en_zona}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f'Total coches: {len(coches_detectados_totalmente)}', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        # Mostrar el frame
        cv2.imshow('Detección de Coches', frame)

        # Salir si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

# Ejemplo de uso con un archivo de video
if __name__ == "__main__":
    video_path = "ruta_video_prueba.mp4"  # Reemplazar con la ruta correcta
    cap = cv2.VideoCapture(video_path)
    procesar_video(cap)
