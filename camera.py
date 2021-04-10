import cv2

# init camera
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,900)
cap.set(10,300)

# init face detection
face_cascade = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml')

while True:
    success,img =cap.read()
    if img is None:
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print(img.shape)# Draw bounding box to imput image.
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        imgCropped = img[ y:y + h,x:x + w]
        cv2.imshow('img', imgCropped)
    #cv2.imwrite("test.jpg",img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break