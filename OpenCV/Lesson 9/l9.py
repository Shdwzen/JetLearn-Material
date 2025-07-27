import cv2, os
from PIL import Image
#Picture to video
os.chdir("C:\\Users\\Admin\\Documents\\JetLearn\\Projects\\OpenCV\\Lesson 9\\Pictures")
path = "C:\\Users\\Admin\\Documents\\JetLearn\\Projects\\OpenCV\\Lesson 9\\Pictures"

Mean_H = 0
Mean_W = 0

Num_Of_Imgs = len(os.listdir("."))

print(Num_Of_Imgs)

for i in os.listdir("."):
    Img = Image.open(os.path.join(path, i))
    Width, Height = Img.size
    Mean_W += Width
    Mean_H += Height

Mean_W = Mean_W//Num_Of_Imgs
Mean_H = Mean_H//Num_Of_Imgs

for i in os.listdir("."):
    if i.endswith(".png") or i.endswith(".jpg"):
        Img = Image.open(os.path.join(path, i))
        Width, Height = Img.size
        resize = Img.resize((Mean_W, Mean_H),Image.LANCZOS)
        resize.save(i,"jpeg",quality=90)
        print(str(Img.filename.split("\\")[-1]),"is Resized")

def video_maker():
    OutputFolder = "C:\\Users\\Admin\\Documents\\JetLearn\\Projects\\OpenCV\\Lesson 9\\"
    VideoName = os.path.join(OutputFolder,"Travel_Tour_Slideshow.avi")
    os.chdir("C:\\Users\\Admin\\Documents\\JetLearn\\Projects\\OpenCV\\Lesson 9\\Pictures")
    Images = []
    for img in os.listdir("."):
        if img.endswith(".png") or img.endswith(".jpg"):
            Images.append(img)
    print(Images)
    frame = cv2.imread(os.path.join(".",Images[0]))
    Height,Width,Layers = frame.shape
    Video = cv2.VideoWriter(VideoName,0,0,2,(Height,Width))
    for i in Images:
        Video.write(cv2.imread(os.path.join(".",i)))
    cv2.destroyAllWindows()
    Video.release()

video_maker()






