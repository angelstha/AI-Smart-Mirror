import cv2
import os
import face_recognition

def load_known_faces(known_faces_dir):
    encodings = []
    names = []
    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
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
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Guest"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        faces.append((top, right, bottom, left, name))
    return faces

def run_face_detection(known_face_encodings, known_face_names, greeting_callback):
    video_capture = cv2.VideoCapture(0)
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
                for (_, _, _, _, name) in faces:
                    greeting_callback(f"Hello {name}!")
            else:
                greeting_callback("Hello Guest!")  # fallback if no match
        process_this_frame = not process_this_frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()