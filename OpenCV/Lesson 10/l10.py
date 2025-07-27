import cv2, numpy, time
Frame_Count = 0


Vid_Output = cv2.VideoCapture("Lesson 10\\video.mp4")
for i in range(60):
    Return_Val,BGround = Vid_Output.read()
    if Return_Val==False:
        continue

while Vid_Output.isOpened():
    Return_Val, FGround = Vid_Output.read()
    if not Return_Val:
        break
    Frame_Count += 1
    HSV = cv2.cvtColor(FGround,cv2.COLOR_BGR2HSV)
    Lower_Red1 = numpy.array([0,20,20])
    Lower_Red2 = numpy.array([0,250,250])
    Mask1 = cv2.inRange(HSV,Lower_Red1,Lower_Red2)
    Higher_Red1 = numpy.array([140,20,20])
    Higher_Red2 = numpy.array([180,250,250])
    Mask2 = cv2.inRange(HSV,Higher_Red1,Higher_Red2)
    Mask = Mask1+Mask2
    Mask = cv2.morphologyEx(Mask,cv2.MORPH_OPEN,numpy.ones((3,3),numpy.uint8),iterations=2)
    Mask = cv2.dilate(Mask,numpy.ones((3,3),numpy.uint8),iterations=1)
    Reversed_Mask = cv2.bitwise_not(Mask)
    Result1 = cv2.bitwise_and(BGround,BGround,mask=Mask)
    Result2 = cv2.bitwise_and(FGround,FGround,mask=Reversed_Mask)
    Output = cv2.addWeighted(Result1,1,Result2,1,0)

    cv2.imshow("Invisible Man",Result2)
    x = cv2.waitKey(10)
    if x == 27:
        cv2.destroyAllWindows()
        break







    