import face_recognition
import os
import numpy as np
import cv2

def load_known_faces(folder):
    encodings, names = [], []
    for filename in os.listdir(folder):
        if filename.endswith((".jpg", ".png")):
            image = face_recognition.load_image_file(os.path.join(folder, filename))
            face_enc = face_recognition.face_encodings(image)
            if face_enc:
                encodings.append(face_enc[0])
                names.append(os.path.splitext(filename)[0].capitalize())
    return encodings, names

def detect_and_recognize(frame, known_encodings, known_names):
    # ✅ Resize using OpenCV, not face_recognition
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    results = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Guest"
        if known_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.8)
            distances = face_recognition.face_distance(known_encodings, face_encoding)
            if len(distances) > 0:
                best_match = np.argmin(distances)
                if matches[best_match]:
                    name = known_names[best_match]

        # Scale back up
        top *= 4; right *= 4; bottom *= 4; left *= 4
        results.append((top, right, bottom, left, name))
    return results