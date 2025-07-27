import cv2, numpy

img = cv2.imread("Lesson 1\pika_image.png")

row,col = img.shape[0:2]

img_rotation = cv2.getRotationMatrix2D((row/2,col/2),90,0.8)
img_rotated = cv2.warpAffine(img,img_rotation,(row,col))

cv2.imshow("chiken",img_rotated)
cv2.waitKey(0)