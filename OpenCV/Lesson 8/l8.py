import cv2, numpy

img = cv2.imread("Lesson 8/blob.jpg",0)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 1350
params.filterByCircularity = True
params.minCircularity = 0.9
params.filterByConvexity = True
params.minConvexity = 0.1
params.filterByInertia = True
params.minInertiaRatio = 0.1

Detector = cv2.SimpleBlobDetector_create(params)
Blob_Img = Detector.detect(img)

BlobCanvas = numpy.zeros((1,1))
Blobs = cv2.drawKeypoints(img,Blob_Img,BlobCanvas,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

BlobNum = len(Blob_Img)
text = str(BlobNum)
cv2.putText(Blobs,text,(50,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow("hi",Blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()