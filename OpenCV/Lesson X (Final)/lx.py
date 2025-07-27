import cv2, os, numpy
HAAR_File =  "E:\JetLearn\Projects\OpenCV\Lesson X (Final)\haarcascade_frontalface_default.xml"
DTsets =  "E:\JetLearn\Projects\OpenCV\Lesson X (Final)\datasets"
Images = []
Labels = []
Name = {}

ID = 0

for (subdir,direc,files) in os.walk(DTsets):
    for subdir in direc:
        Name[ID] = subdir
        path = os.path.join(DTsets,subdir)
        for file in os.listdir(path):
            curr_path = path + '/' + file
            lbl = ID
            Images.append(cv2.imread(curr_path,0))
            Labels.append(lbl)
        ID += 1

print(Images)
Width,Height = 130,100
(Images,Labels) = [numpy.array(i) for i in [Images,Labels]]
#OpenCV Training model
Recogniser = cv2.face.LBPHFaceRecognizer_create()
Recogniser.train(Images,Labels)

#Recogniser linked to cam
FaceCascade = cv2.CascadeClassifier(HAAR_File)
Webcam = cv2.VideoCapture(1)
while True:
    _,val = Webcam.read()
    newVal = cv2.cvtColor(val,cv2.COLOR_BGR2GRAY)
    Faces = FaceCascade.detectMultiScale(newVal,1.3,3)
    for (x,y,w,h) in Faces:
        face = newVal[y:y + h, x:x + w]
        face_resize = cv2.resize(face,(Width,Height))
        prediction = Recogniser.predict(face_resize)
        if prediction[1]<120:
            cv2.putText(val, '% s - %.0f' % (Name[prediction[0]], prediction[1]),(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,250,0))
            cv2.rectangle(val,(x,y),(x+w,y+h),(0,250,0),5)
        else: 
            cv2.putText(val,"Not Recognised!",(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,250))
            cv2.rectangle(val,(x,y),(x+w,y+h),(0,0,250),5)
    cv2.imshow("Face Scanner",val)
    key = cv2.waitKey(10)
    if key == 27:
        break