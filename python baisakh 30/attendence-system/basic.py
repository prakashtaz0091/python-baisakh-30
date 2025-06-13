import cv2

# basic image reading

# img = cv2.imread("test.png")
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# basic frontal face recognition

face_cascade = cv2.CascadeClassifier(
    "venv/lib/python3.12/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"
)

# original image
img = cv2.imread("group.png")

# gray image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
# Detect faces in the gray image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=4)
# scaleFactor is a parameter specifying how much the image size is reduced at each image scale.
# The larger the scale factor is, the less the image is reduced, and the longer it takes to detect faces.
# minNeighbors is a parameter specifying how many neighbors each candidate rectangle should have to retain it.
# The more neighbors you require, the more accurate the detection is, but the longer it takes.

# # show rectangles for faces
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
