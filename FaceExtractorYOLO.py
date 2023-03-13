import torch
import cv2
import numpy as np


class FaceExtractorYOLO():

    def __initNN(self):
        self.model = torch.hub.load('WongKinYiu/yolov7', 'custom', path_or_model='models/last.pt', force_reload=True)
        pass


    def recognize(self,img):

        results = self.model(img)
        boxes = results.pred[0][:, :4]
        confidences = results.pred[0][:, 4]
        class_ids = results.pred[0][:, 5]


        img_with_box = img.copy()
        faces = []
        for i in range(len(boxes)):
            if int(class_ids[i]) == 0:
                x1, y1, x2, y2 = boxes[i]
                faces.append(img[int(y1):int(y2) ,int(x1):int(x2)])
                img_with_box = cv2.rectangle(img_with_box,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),3)
        return (img_with_box,faces)
    
    def __init__(self):
        self.__initNN()