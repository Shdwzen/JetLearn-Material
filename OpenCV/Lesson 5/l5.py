import cv2, numpy
img = cv2.imread("Lesson 5/imagegrey.webp",-1)
clr_img = cv2.imread("Lesson 5/umbrella.webp",-1)

img_color = cv2.cvtColor(clr_img,cv2.COLOR_BGR2RGB)

b,g,r = cv2.split(img_color)
"""
cv2.imshow("stret",img)
cv2.waitKey(0)"""

row,col = img_color.shape[0:2]
for y in range(row):
    for x in range(col):
        avr = sum(img_color[y,x])/3
        img_color[y,x] = [avr,avr,avr]



print(img_color.shape)
print("\n"+str(img_color))

cv2.imshow("blue",img_color)
cv2.waitKey(0)
