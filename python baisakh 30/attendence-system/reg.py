import cv2
import face_recognition
import pickle

# Step 1: Capture image from webcam
cap = cv2.VideoCapture(0)

print("Capturing face... Look at the camera!")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # Detect face locations
    face_locations = face_recognition.face_locations(frame)

    # Draw green rectangle around each detected face
    for top, right, bottom, left in face_locations:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Show the frame to the user
    cv2.imshow("Face Capture", frame)

    # Press 's' to save the face
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

cap.release()
cv2.destroyAllWindows()


# Step 2: Detect face and encode
if len(face_locations) == 0:
    print("No face detected! Try again.")
    exit()
elif len(face_locations) > 1:
    print("Multiple faces detected! Ensure only one face is visible.")
    exit()


# Encoding the face
face_encodings = face_recognition.face_encodings(frame, face_locations)
# print(face_encodings)
name = input("Enter name for this face: ")

# Step 3: Save encodings to file
try:
    with open("encodings.pickle", "rb") as file:
        known_faces = pickle.load(file)
except FileNotFoundError:
    known_faces = {}


# known_faces = {'ram':face_enc}
# known_faces['prakash'] = new_face_enc
known_faces[name] = face_encodings[0]

with open("encodings.pickle", "wb") as file:
    pickle.dump(known_faces, file)

print(f"Face for {name} saved successfully!")
