#!/bin/bash
pip install -r requirements.txt
git clone https://github.com/WongKinYiu/yolov7.git
mkdir models
wget https://github.com/Xevi8X/WTUM_2023_gr5/releases/download/23.03.2023/yolo.pt -P ./models
wget https://github.com/Xevi8X/WTUM_2023_gr5/releases/download/23.03.2023/haar.xml -P ./models
wget https://github.com/Xevi8X/WTUM_2023_gr5/releases/download/23.03.2023/CNN_JC.h5 -P ./models
