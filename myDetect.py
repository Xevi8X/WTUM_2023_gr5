import torch
import cv2
import numpy as np

model = torch.hub.load('WongKinYiu/yolov7', 'custom', path_or_model='models/last.pt', force_reload=True)

img = cv2.imread('family.jpg')

img = np.array(img)

    # Apply the YOLOv7 model on the image
results = model(img)

    # Extract the coordinates of the detected faces
boxes = results.pred[0][:, :4]
confidences = results.pred[0][:, 4]
class_ids = results.pred[0][:, 5]

img_with_box = img.copy()
faces = []
for i in range(len(boxes)):
    if int(class_ids[i]) == 0:  # 0 is the index of the face class in YOLOv7
        x1, y1, x2, y2 = boxes[i]
        faces.append([int(x1), int(y1), int(x2 - x1), int(y2 - y1)])
        img_with_box = cv2.rectangle(img_with_box,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),3)


cv2.imshow('test',img_with_box)
cv2.waitKey(0)