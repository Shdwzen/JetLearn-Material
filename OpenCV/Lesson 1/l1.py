import cv2
img=cv2.imread('Lesson 1/pika_image.png',cv2.IMREAD_UNCHANGED)
#cv2.IMREAD_COLOR = To load image in color (Can also replace with 1)
#cv2.IMREAD_GRAYSCALE = To load image in Grayscale (Can also replace with 0)
#cv2.IMREAD_UNCHANGED = To Load image unchanged (Can also replace with -1)


"""cv2.imshow("Pikachu image",img)
#to hold window until user presses a key
cv2.waitKey(0)
cv2.destroyAllWindows()"""

#Print image in different colour formats
#RGB = BGR (flipped)

B,G,R = cv2.split(img)
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.imshow("Blue saturation",B)
cv2.waitKey(0)
cv2.imshow("Green saturation",G)
cv2.waitKey(0)
cv2.imshow("Red saturation",R)
cv2.waitKey(0)
cv2.destroyAllWindows()
