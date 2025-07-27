import cv2, numpy

img = cv2.imread("Lesson 5/umbrella.webp",-1)

Blurred = cv2.GaussianBlur(img,(5,5),0)
Edges_Low = cv2.Canny(Blurred,threshold1=10,threshold2=100)
Edges_High = cv2.Canny(Blurred,threshold1=150,threshold2=200)

cv2.imshow("Edges",Edges_Low)
cv2.imshow("H-Edges",Edges_High)

cv2.waitKey(0)
