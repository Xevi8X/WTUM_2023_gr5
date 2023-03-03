import cv2 as cv
from FaceExtractor import FaceExtractor

def main():
    fe = FaceExtractor()
    img = cv.imread("img/family.jpg")
    (img_with_box, faces) = fe.recognize(img)
    cv.imshow('test',img_with_box)
    cv.waitKey(0)



if __name__ == '__main__':
    main()
