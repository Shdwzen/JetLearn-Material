import cv2, numpy

img = cv2.imread("Lesson 1\pika_image.png")

"""start = (0,0)
end = (200,200)
line_thickness = 3
color = (0,1,150)
font = cv2.FONT_HERSHEY_COMPLEX

#lined_img = cv2.line(img,start,end,color,line_thickness)
rect_img = cv2.rectangle(img,start,end,color,line_thickness)
crcl_img = cv2.circle(img,end,150,color,line_thickness)
txt_img = cv2.putText(img,"hi lol",end,font,20,color,line_thickness,cv2.LINE_AA)

cv2.imshow("hi",txt_img)
cv2.waitKey(0)
"""



Grey_Img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Blur_Img = cv2.blur(Grey_Img,(3,3))
HCircle = cv2.HoughCircles(Blur_Img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)

if HCircle is not None:
    HCircle = numpy.uint16(numpy.around(HCircle))
    for i in HCircle[0,:]:
        x,y,r =  i[0],i[1],i[2]
        cv2.circle(img,(x,y),r,(0,200,50),2)
        cv2.circle(img,(x,y),1,(0,50,200),2)
        cv2.imshow("crcl",img)
        cv2.waitKey(0)

cv2.destroyAllWindows()