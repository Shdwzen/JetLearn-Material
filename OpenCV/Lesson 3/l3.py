import cv2, numpy

"""
img = cv2.imread("Lesson 2\planet.jpg")
cv2.imshow("Image hehe",img)
cv2.waitKey(0)
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Grey nooo",grey_img)
cv2.waitKey(0)
"""

img = cv2.imread("Lesson 2\planet.jpg")

""" --Average img value with low weight
------------------------------------------------
#Find dimensions of image & color var
row,col,clr = img.shape[0:3] #List slicing to find the 0th and 1st value of .shape
for i in range(row):
    for g in range(col):
        for c in range(clr):
            img[i,g,c] = sum(img[i,g])*0.33
"""

""" -- HSV Color Value
---------------------------------
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#Find dimensions of image & color var
hsv_img[:,:,1] = numpy.clip(hsv_img[:,:,1]*1,20,150)

img_alt = cv2.cvtColor(hsv_img,cv2.COLOR_HSV2BGR)


cv2.imshow("hsv something",hsv_img)
cv2.waitKey(0)
cv2.imshow("bgr something",img_alt)
cv2.waitKey(0)
"""
