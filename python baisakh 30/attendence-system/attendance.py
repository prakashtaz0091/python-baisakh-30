import cv2
import face_recognition
import pickle
from datetime import datetime
import csv

# Step 1: Capture image from webcam
cap = cv2.VideoCapture(0)

try:
    with open("encodings.pickle", "rb") as file:
        known_faces = pickle.load(file)
except FileNotFoundError:
    known_faces = {}


today_attendance_filename = f"{datetime.now().strftime('%Y-%m-%d')}_attendance.csv"
today_attendance = []


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

    # Step 2: Detect face and encode
    if len(face_locations) > 0:
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        # print(len(face_encodings), " faces found")
        for current_face in face_encodings:
            for name, face_encoding in known_faces.items():
                if face_recognition.compare_faces([face_encoding], current_face):
                    new_attendance = [name, str(datetime.now().strftime("%H:%M:%S"))]

                    already_attended_names = [
                        attendace_data[0] for attendace_data in today_attendance
                    ]
                    if new_attendance[0] not in already_attended_names:
                        today_attendance.append(new_attendance)

    # # Press 'Esc' to quit the attendance
    if cv2.waitKey(1) & 0xFF == 27:
        break


with open(today_attendance_filename, "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Time"])
    writer.writerows(today_attendance)

cap.release()
cv2.destroyAllWindows()
