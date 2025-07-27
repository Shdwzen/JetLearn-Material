import cv2, numpy

snow_img = cv2.imread("Lesson 2/snow.jpg")
planet_img = cv2.imread("Lesson 2/planet.jpg")
pika_img = cv2.imread("Lesson 1/pika_image.png")

# img_weight = cv2.addWeighted(snow_img,0.3,planet_img,0.7,0)
# img_weight = cv2.subtract(snow_img,planet_img)
#img_weight = cv2.resize(snow_img,(200,200))
#krnl = numpy.ones((1,50),numpy.uint8)
#img_weight = cv2.erode(pika_img,krnl)

#Gaussian Blur
#img_weight = cv2.GaussianBlur(pika_img,(7,5),2)

#Median Blur
#img_weight = cv2.medianBlur(pika_img,7)

#Bilateral Filter
#img_weight = cv2.bilateralFilter(pika_img,30,120,180)

#Image Border
#img_weight = cv2.imread("Lesson 1/pika_image.png")
#img_border = cv2.copyMakeBorder(img_weight,100,100,100,100,cv2.BORDER_REFLECT,value=1)

cv2.imshow("Normal",pika_img)
cv2.imshow("Changed",img_border)
cv2.waitKey(0)
cv2.destroyAllWindows()