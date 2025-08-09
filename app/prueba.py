

# import cv2
# import mediapipe as mp
# import numpy as np
# import time

# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose

# # Función para calcular ángulo entre tres puntos
# def calculate_angle(a, b, c):
#     a = np.array(a)
#     b = np.array(b)
#     c = np.array(c)

#     radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
#     angle = np.abs(radians*180.0/np.pi)
    
#     if angle > 180.0:
#         angle = 360 - angle
        
#     return int(angle)

# # Configuración inicial
# cap = cv2.VideoCapture(0)
# good_posture_start = None
# good_posture_time = 0

# with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         # Convertir a RGB
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         image.flags.writeable = False
#         results = pose.process(image)
        
#         # Volver a BGR
#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#         try:
#             landmarks = results.pose_landmarks.landmark
            
#             # Coordenadas de puntos clave
#             ear = [landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x,
#                    landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y]
#             shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
#                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
#             hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
#                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
#             knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
#                     landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

#             # Calcular ángulos
#             neck_angle = calculate_angle(shoulder, ear, [shoulder[0], shoulder[1]-0.1])
#             torso_angle = calculate_angle(shoulder, hip, knee)

#             # Dibujar líneas y puntos
#             h, w, _ = image.shape
#             ear_px = tuple(np.multiply(ear, [w, h]).astype(int))
#             shoulder_px = tuple(np.multiply(shoulder, [w, h]).astype(int))
#             hip_px = tuple(np.multiply(hip, [w, h]).astype(int))
#             knee_px = tuple(np.multiply(knee, [w, h]).astype(int))

#             cv2.line(image, ear_px, shoulder_px, (0,255,0), 2)
#             cv2.line(image, shoulder_px, hip_px, (0,255,0), 2)
#             cv2.circle(image, ear_px, 5, (0,255,255), -1)
#             cv2.circle(image, shoulder_px, 5, (0,255,255), -1)
#             cv2.circle(image, hip_px, 5, (0,255,255), -1)
#             cv2.circle(image, knee_px, 5, (0,255,255), -1)

#             # Mostrar valores de ángulo
#             cv2.putText(image, str(neck_angle), shoulder_px,
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)
#             cv2.putText(image, str(torso_angle), hip_px,
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)

#             # Estado de postura
#             if neck_angle < 55 and torso_angle < 15:
#                 if good_posture_start is None:
#                     good_posture_start = time.time()
#                 posture_status = "Aligned"
#                 posture_color = (0,255,0)
#             else:
#                 good_posture_start = None
#                 posture_status = "Bad posture"
#                 posture_color = (0,0,255)

#             # Tiempo acumulado de buena postura
#             if good_posture_start:
#                 good_posture_time = time.time() - good_posture_start

#             # Mostrar estado
#             cv2.putText(image, posture_status, (w-150, 30),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1, posture_color, 2, cv2.LINE_AA)
#             cv2.putText(image, f"Good Posture Time: {good_posture_time:.1f}s",
#                         (10, h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)

#         except:
#             pass
        
#         cv2.imshow('Posture Analysis', image)

#         if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
#             break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp

# # Inicializa MediaPipe Pose
# mp_pose = mp.solutions.pose
# pose = mp_pose.Pose()
# mp_drawing = mp.solutions.drawing_utils

# # Abre la cámara
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convierte a RGB
#     image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = pose.process(image_rgb)

#     if results.pose_landmarks:
#         mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

#         h, w, _ = frame.shape

#         # Ancho de hombros (en píxeles)
#         hombro_izq_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * w
#         hombro_der_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * w
#         ancho_hombros_px = abs(hombro_der_x - hombro_izq_x)

#         # Ancho de caderas (en píxeles)
#         cadera_izq_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x * w
#         cadera_der_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x * w
#         ancho_caderas_px = abs(cadera_der_x - cadera_izq_x)

#         # Relación hombros/caderas
#         rel_hombros_caderas = ancho_hombros_px / ancho_caderas_px if ancho_caderas_px > 0 else 0

#         # Clasificación rápida de contextura
#         if ancho_hombros_px < 200 and ancho_caderas_px < 200:
#             contextura = "Delgado"
#         elif 200 <= ancho_hombros_px <= 300:
#             contextura = "Normal"
#         else:
#             contextura = "Robusto"

#         # Mostrar resultados
#         cv2.putText(frame, f"Contextura: {contextura}", (10, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#         cv2.putText(frame, f"Hombros(px): {ancho_hombros_px:.0f}", (10, 80),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
#         cv2.putText(frame, f"Caderas(px): {ancho_caderas_px:.0f}", (10, 110),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
#         cv2.putText(frame, f"H/C: {rel_hombros_caderas:.2f}", (10, 140),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 165, 255), 2)

#     # Mostrar ventana
#     cv2.imshow("Deteccion de Contextura", frame)

#     # Salir con ESC
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()
