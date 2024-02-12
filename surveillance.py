import cv2
import face_recognition

# Load sample images for face recognition (replace with the actual paths)
known_images = [
    face_recognition.load_image_file('sri pic.jpg'),
    face_recognition.load_image_file('vt.jpg')
    
]

# Encode the known faces
known_face_encodings = [face_recognition.face_encodings(img)[0] for img in known_images]

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Find face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        # Compare detected face with the known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"
        for i, match in enumerate(matches):
            if match:
                name = f"Person {i + 1}"
                break

        # Display a rectangle around the detected face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        # Display the name on the frame
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera when everything is done
cap.release()
cv2.destroyAllWindows()
