import cv2, numpy

Red = numpy.array([0,200,0])
Green = numpy.array([200,0,0])

R_Box = numpy.full((300,300,3),Red,dtype=numpy.uint8)
G_Box = numpy.full((300,300,3),Green,dtype=numpy.uint8)

R_Box = cv2.cvtColor(R_Box,cv2.COLOR_BGR2RGB)
G_Box = cv2.cvtColor(G_Box,cv2.COLOR_BGR2RGB)

Mix_Box = cv2.add(R_Box,G_Box)
Mix_Box2 = cv2.subtract(R_Box,G_Box)

Mix_Boxes = numpy.concatenate((R_Box,G_Box,Mix_Box,Mix_Box2),axis=1)

cv2.imshow("Added",Mix_Box)
cv2.waitKey(0)
cv2.imshow("Subtracted",Mix_Box2)
cv2.waitKey(0)
cv2.imshow("combined",Mix_Boxes)
cv2.waitKey(0)
cv2.destroyAllWindows()
