import cv2 as cv
import matplotlib.pyplot as plt

def init_NN():
    c = cv.CascadeClassifier()
    c.load(cv.samples.findFile("haarcascade_frontalface_alt.xml"))
    return c

def recognize(img):


    gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray_img = cv.equalizeHist(gray_img)
    faces_coords = cascade.detectMultiScale(gray_img)

    print('Detected faces: ' + str(len(faces_coords)))

    img_with_box = img.copy()
    faces = []
    for (x,y,w,h) in faces_coords:
        img_with_box = cv.rectangle(img_with_box,(x,y),(x+w,y+h),(0,255,0),3)
        faces.append(img[y:y+h,x:x+h])
    return (img_with_box,faces)


cascade = init_NN()
img = cv.imread("family.jpg")
(img_with_box, faces) = recognize(img)

cv.imshow('test',img_with_box)
cv.waitKey(0)

