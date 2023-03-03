import cv2 as cv
import matplotlib.pyplot as plt

class FaceExtractor():

    def __initNN(self):
        self.cascade = cv.CascadeClassifier()
        self.cascade.load(cv.samples.findFile("haarcascade_frontalface_alt.xml"))

    def recognize(self,img):
        gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        gray_img = cv.equalizeHist(gray_img)
        faces_coords = self.cascade.detectMultiScale(gray_img)
        print('Detected faces: ' + str(len(faces_coords)))

        img_with_box = img.copy()
        faces = []
        for (x,y,w,h) in faces_coords:
            img_with_box = cv.rectangle(img_with_box,(x,y),(x+w,y+h),(0,255,0),3)
            faces.append(img[y:y+h,x:x+h])
        return (img_with_box,faces)
    
    def __init__(self):
        self.__initNN()

