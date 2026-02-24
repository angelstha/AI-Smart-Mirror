import cv2
import os
import face_recognition

def load_known_faces(known_faces_dir):
    encodings = []
    names = []
    for filename in os.listdir(known_faces_dir):
        if filename.lower().endswith((".jpg", ".png")):
            path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(path)
            encodings_list = face_recognition.face_encodings(image)
            if encodings_list:  # only add if a face was found
                encodings.append(encodings_list[0])
                names.append(os.path.splitext(filename)[0])  # filename as name
    return encodings, names


def detect_and_recognize(frame, known_face_encodings, known_face_names):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    faces = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

        name = "Guest"
        if len(face_distances) > 0:
            best_match_index = face_distances.argmin()
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        faces.append((top, right, bottom, left, name))
    return faces


def run_face_detection(known_face_encodings, known_face_names, greeting_callback):
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Could not open camera")
        return

    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Camera not returning frames")
            break

        if process_this_frame:
            faces = detect_and_recognize(frame, known_face_encodings, known_face_names)
            print("Detected faces:", faces)  # Debug line

            if faces:
                for (top, right, bottom, left, name) in faces:
                    greeting_callback(f"Hello {name}!")

                    # Draw bounding box
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    # Draw label
                    cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, name, (left + 6, bottom - 6),
                                cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0), 1)
            else:
                greeting_callback("Hello Guest!")  # fallback if no match

        process_this_frame = not process_this_frame

        # Show the video feed with overlays
        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    known_encodings, known_names = load_known_faces("known_faces")

    def greet(msg):
        print(msg)

    run_face_detection(known_encodings, known_names, greet)	