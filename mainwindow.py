from PyQt6.QtWidgets import QApplication, QMainWindow,QMenuBar, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QScrollArea,QFrame, QFileDialog
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
import cv2
import numpy as np

from Face import Face
from FaceExtractor import FaceExtractor
from EmotionRecognizer import EmotionRecognizer



def cv2ImageToQLabel(image,out_width=600,out_height=400):
    height, width, channel = image.shape
    bytesPerLine = 3 * width
    convert = QImage(image.astype(np.uint8), width, height, bytesPerLine, QImage.Format.Format_BGR888)
    #convert = QImage(image.data, image.shape[1], image.shape[0], image.strides[0], QImage.Format.Format_BGR888)
    convert = convert.scaled(out_width,out_height,aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    frame = QLabel()
    frame.setPixmap(QPixmap.fromImage(convert))
    #frame.setScaledContents(False)
    return frame

class Images_VLayoutWidget(QWidget):
     def __init__(self, image_before,image_after):
        super().__init__()
        self.mylayout = QVBoxLayout()
        self.mylayout.addWidget(QLabel("Orginal image:"))
        self.mylayout.addWidget(image_before)
        self.mylayout.addWidget(QLabel("Recognized face:"))
        self.mylayout.addWidget(image_after)
        self.setLayout(self.mylayout)
        self.setFixedWidth(700)

class FaceEmotion(QFrame):
     def __init__(self, face: Face):
        super().__init__()
        self.setFixedSize(550,260)
        self.setStyleSheet("QFrame {background-color: rgb(90, 90, 90);"
                                "border-width: 1;"
                                "border-radius: 3;"
                                "border-style: solid;"
                                "border-color: rgb(90, 90, 90)}"
                                )
        #self.setStyleSheet("border: 3px solid green;")
        label = cv2ImageToQLabel(face.img,256,256)
        
        
        pred = ""
        percent = ""
        for emotion in face.rec_emotion:
            if emotion[1] > 0:
                pred = pred + emotion[0]+":\n"
                percent = percent + f'{emotion[1]:.2f}%\n'
        hlayout = QHBoxLayout()
        hlayout.addWidget(label)
        hlayout.addWidget(QLabel(pred))
        hlayout.addWidget(QLabel(percent))
        self.setLayout(hlayout)
        

class Scroll_VLayoutWidget(QWidget):
     def __init__(self,faces):
        super().__init__()
        list = QVBoxLayout()
        for face in faces:
            list.addWidget(FaceEmotion(face))

        widget = QWidget()
        widget.setLayout(list)

        scrollArea = QScrollArea()
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scrollArea.setWidget(widget)

        self.mylayout = QVBoxLayout()
        self.mylayout.addWidget(QLabel("Emotions:"))
        self.mylayout.addWidget(scrollArea)
        self.setLayout(self.mylayout)
        self.setFixedWidth(600)

class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()

        self.faceExtractor = FaceExtractor()
        self.emotionRecognizer = EmotionRecognizer()
        self.faces = [] 

        self.app = app
        self.setFixedSize(1400,1000)
        self.setWindowTitle("Emotion recognizer")
        self.img_before = self.placeholder()
        self.img_after = self.placeholder()
        self.render()
        menu_bar = self.menuBar()
        load_action = menu_bar.addAction("&Load")
        load_action.triggered.connect(self.load)
        load_action = menu_bar.addAction("Recognize &faces")
        load_action.triggered.connect(self.recognizeFaces)
        load_action = menu_bar.addAction("Recognize &emotion")
        load_action.triggered.connect(self.recognizeEmotion)
        quit_action = menu_bar.addAction("&Clear")
        quit_action.triggered.connect(self.clear)
        quit_action = menu_bar.addAction("&Quit")
        quit_action.triggered.connect(lambda: self.app.quit())
    
    def load(self):
        dlg = QFileDialog()
        dlg.exec()
        files = dlg.selectedFiles()
        self.orginalImg = cv2.imread(files[0])
        #self.orginalImg = cv2.imread("img/family.jpg")
        self.img_before = cv2ImageToQLabel(self.orginalImg)
        self.render()

    def recognizeFaces(self):
        (self.image_with_box,face_imgs) = self.faceExtractor.recognize(self.orginalImg)
        for face_img in face_imgs:
            self.faces.append(Face(face_img))
        self.img_after = cv2ImageToQLabel(self.image_with_box)
        self.render()

    def recognizeEmotion(self):
        for face in self.faces:
            rec_emotion = self.emotionRecognizer.recognize(face)
            face.setEmotion(rec_emotion)
        self.render()
    
    def clear(self):
        self.orginalImg = np.zeros((1,1,3), np.uint8)
        self.image_with_box = np.zeros((1,1,3), np.uint8)
        self.img_before = self.placeholder()
        self.img_after = self.placeholder()
        self.faces = []
        self.render()

    def placeholder(self):
        placeHolder = QLabel()
        placeHolder.setFixedSize(800,400)
        return placeHolder
        



    def render(self):
    
        h_layout = QHBoxLayout()
        h_layout.addWidget(Images_VLayoutWidget(self.img_before,self.img_after))
        h_layout.addWidget(Scroll_VLayoutWidget(self.faces))

        central = QWidget()
        central.setLayout(h_layout)
        self.setCentralWidget(central)
