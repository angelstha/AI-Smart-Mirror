import cv2
from datetime import datetime
from faces import load_known_faces, detect_and_recognize
from weather import get_weather
from ui import draw_dashboard, draw_greeting

# -------------------------------
# Load known faces
# -------------------------------
known_face_encodings, known_face_names = load_known_faces("known_faces")

# -------------------------------
# Start camera
# -------------------------------
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cv2.namedWindow("Smart Mirror AI", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Smart Mirror AI", 1280, 720)

process_this_frame = True
last_faces = []

# -------------------------------
# Main loop
# -------------------------------
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Run recognition every other frame
    if process_this_frame:
        last_faces = detect_and_recognize(frame, known_face_encodings, known_face_names)
    process_this_frame = not process_this_frame

    # Draw greetings for each face
    for (top, right, bottom, left, name) in last_faces:
        draw_greeting(frame, top, right, bottom, left, name)

    # Date, time, weather
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%A, %d %B %Y")
    weather_info = get_weather(city="Kathmandu")

    draw_dashboard(frame, current_date, current_time, weather_info)

    # Show the frame
    cv2.imshow("Smart Mirror AI", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------------------
# Cleanup
# -------------------------------
video_capture.release()
cv2.destroyAllWindows()