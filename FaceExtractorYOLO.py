import torch
import cv2
import numpy as np


class FaceExtractorYOLO():

    def __initNN(self):
        self.model = torch.hub.load('WongKinYiu/yolov7', 'custom', path_or_model='models/yolo.pt', force_reload=True)
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
                w = int(x2) - int(x1)
                h = int(y2) - int(y1)
                x_center = (int(x2) + int(x1))//2
                y_center = (int(y2) + int(y1))//2
                a = max(w,h)//2
                #TODO: zabezpieczyc przed wyjsciem poza zakres
                y_up = y_center - a
                y_down = y_center + a
                x_left = x_center - a
                x_right = x_center + a
                
                # fix x
                if x_left < 0:
                    xd = -x_left
                    x_left += xd
                    x_right += xd
                elif x_right >= img.shape[1]:
                    xd = x_right - img.shape[1] + 1
                    x_left -= xd
                    x_right -= xd

                # fix y
                if y_down < 0:
                    yd = -y_down
                    y_down += yd
                    y_up += yd
                elif y_up >= img.shape[0]:
                    yd = y_up - img.shape[0] + 1
                    y_down -= yd
                    y_up -= yd


                faces.append(img[y_up:y_down ,x_left:x_right])
                img_with_box = cv2.rectangle(img_with_box,(x_left,y_up),(x_right,y_down),(0,255,0),3)

        return (img_with_box,faces)
    
    def __init__(self):
        self.__initNN()