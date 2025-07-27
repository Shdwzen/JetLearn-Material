import cv2, os

HAAR_File = "E:/JetLearn/Projects/OpenCV/Lesson 12/haarcascade_frontalface_default.xml"
Path = "E:/JetLearn/Projects/OpenCV\Lesson 12\datasets\Placeholder" #Insert name here

if not os.path.isdir(Path):
    os.mkdir(Path)

width, height = (200,190)
Face_Casc = cv2.CascadeClassifier(HAAR_File)

Webcam = cv2.VideoCapture(1)
Frame_Count = 1
while Frame_Count < 31:
    _,val = Webcam.read()
    new_val = cv2.cvtColor(val,cv2.COLOR_BGR2GRAY)
    faces = Face_Casc.detectMultiScale(new_val,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(new_val,(x,y),(x+w,y+h),(250,0,0),2)
        face = new_val[y:y + h, x:x + w]
        face_resize = cv2.resize(face,(width,height))
        cv2.imwrite(f"{Path}\{Frame_Count}.png",face_resize)
    Frame_Count += 1
    #cv2.imshow("Face_DS",val)
    key = cv2.waitKey(10)
    if key == 27:
        break

