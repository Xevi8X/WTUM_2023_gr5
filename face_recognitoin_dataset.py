# import os
# from tensorflow.keras.utils import load_img
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image
# import cv2
# # path_to_dataset = 'C:\Users\YanPC\Desktop\dataset\\'
# # path_iamges_folder = 'img_celeba\\'
# # path_to_bounding_box_file = 'Anno\list_bbox_celeba.txt'
# # path_to_partition_file='Eval\list_eval_partition.txt'


# class face_recognition_dataset:
#     def __init__(self):
#         self.path_to_dataset = r"C:\Users\YanPC\Desktop\dataset"'\\'
#         self.path_images_folder = os.path.join(
#             self.path_to_dataset, r"img_celeba"'\\')
#         self.path_to_bounding_box_file = os.path.join(
#             self.path_to_dataset, r'Anno\list_bbox_celeba.txt')
#         self.path_to_partition_file = os.path.join(
#             self.path_to_dataset, r'Eval\list_eval_partition.txt')

#     def GetImageWithBoundingBox(self,file, bounding_box_line_data):
#         line_color = (0, 0, 0)
#         line_thickness = 3
#         img = np.asarray(Image.open(file))
#         splitted = bounding_box_line_data.split()
#         x, y, width, heigh = int(splitted[1]), int(
#             splitted[2]), int(splitted[3]), int(splitted[4])
#         img = cv2.rectangle(img, (x, y), (x+width, y+heigh),
#                             line_color, line_thickness)
#         return img

#     def LoadDataset(self):
#         bbox_file = open(self.path_to_bounding_box_file, 'r')
#         bbox_lines = bbox_file.readlines()[2:]
        
#         partition_file = open(self.path_to_partition_file, 'r')
#         partition_lines = partition_file.readlines()
        
#         cwd = os.getcwd()
        
#         train_dataset=[]
#         validation_dataset=[]
#         test_dataset=[]
#         os.chdir(self.path_images_folder)
#         for i, file in enumerate(os.listdir('.')):
#             # img = self.GetImageWithBoundingBox(file, bbox_lines[i])
#             # plt.imshow(img)
#             # plt.show()
#             partition_line= partition_lines[i].split()
            
#             if partition_line[1] == '0':
#                 train_dataset.append(0)
#             if partition_line[1] == '1':
#                 validation_dataset.append(1)
#             if partition_line[1] == '2':
#                 test_dataset.append(2)
#             # if i == 1000:
#             #     break
#             print(i)
#         os.chdir(cwd)
#         return train_dataset,validation_dataset,test_dataset

# dataset = face_recognition_dataset()

# res = dataset.LoadDataset()
# print("fienis")
# fdg = 4

import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("coco-2017", split="validation"