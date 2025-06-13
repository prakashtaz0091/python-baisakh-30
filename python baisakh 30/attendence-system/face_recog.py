import face_recognition
import cv2

image = face_recognition.load_image_file("./data/2faces.png")
face_locations = face_recognition.face_locations(image)

face_encodings = face_recognition.face_encodings(image, face_locations)
print(len(face_encodings), " faces found")
print(len(face_encodings[0]))
