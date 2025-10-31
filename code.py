import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

# Eye landmarks
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def get_eye_openness(eye_points, landmarks, img_w, img_h):
    points = [(int(landmarks[p].x * img_w), int(landmarks[p].y * img_h)) for p in eye_points]
    # EAR-like calculation
    vertical1 = np.linalg.norm(np.array(points[1]) - np.array(points[5]))
    vertical2 = np.linalg.norm(np.array(points[2]) - np.array(points[4]))
    horizontal = np.linalg.norm(np.array(points[0]) - np.array(points[3]))
    openness = (vertical1 + vertical2) / (2.0 * horizontal)
    return openness, points

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            lm = face_landmarks.landmark

            left_openness, left_pts = get_eye_openness(LEFT_EYE, lm, w, h)
            right_openness, right_pts = get_eye_openness(RIGHT_EYE, lm, w, h)

            avg_open = (left_openness + right_openness) / 2

            # Define color
            color = (0, 255, 0) if avg_open > 0.2 else (0, 0, 255)
            status = "EYES OPEN" if avg_open > 0.2 else "EYES CLOSED"

            # Draw eye landmarks and outline
            for pts in [left_pts, right_pts]:
                for pt in pts:
                    cv2.circle(frame, pt, 2, color, -1)
                cv2.polylines(frame, [np.array(pts)], isClosed=True, color=color, thickness=1)

            # Show status text
            cv2.putText(frame, status, (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3)

    cv2.imshow("Driver Eye Monitoring", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()


