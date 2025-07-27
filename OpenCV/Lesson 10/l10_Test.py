import cv2
import numpy as np
capture_video = cv2.VideoCapture("Lesson 10\\video.mp4")
count = 0 
for i in range(60):
	return_val , background = capture_video.read()
	if return_val == False :
		continue 
#background = np.flip(background, axis=0)
while (capture_video.isOpened()):
	return_val, img = capture_video.read()
	if not return_val :
		break 
	count = count + 1
#	img = np.flip(img , axis=0)
	hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
	lower_red = np.array([0, 40, 40])
	upper_red = np.array([0, 255, 255])
	mask1 = cv2.inRange(hsv,lower_red,upper_red)

	lower_red = np.array([160, 40, 40])
	upper_red = np.array([180, 255, 255])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	finalmask = mask1+mask2
	finalmask= cv2.morphologyEx(finalmask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
	finalmask = cv2.dilate(finalmask,np.ones((3,3),np.uint8),iterations = 1)
	hideRed = cv2.bitwise_not(finalmask)
	res1 = cv2.bitwise_and(background,background,mask=finalmask)
	res2 = cv2.bitwise_and(img,img,mask=hideRed)
	final_output = cv2.addWeighted(res1,1,res2,1,0)
	cv2.imshow("INVISIBLE MAN",final_output)
	k = cv2.waitKey(10)
	if k == 27:
            break