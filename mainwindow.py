from PyQt6.QtWidgets import QApplication, QMainWindow,QMenuBar, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QScrollArea,QListWidget, QListWidgetItem
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
import cv2


def displayImageWidget():
        image = cv2.imread('img/family.jpg')
        convert = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format.Format_BGR888)
        convert = convert.scaled(600,400,aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        frame = QLabel()
        frame.setPixmap(QPixmap.fromImage(convert))
        #frame.setScaledContents(True)
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

class FaceEmotion(QLabel):
     def __init__(self, face):
        super().__init__()
        self.setFixedSize(550,300)
        self.setStyleSheet("border: 3px solid red;")
        self.setText(str(face))

class Scroll_VLayoutWidget(QWidget):
     def __init__(self,faces):
        super().__init__()
        list = QVBoxLayout()
        

        for face in faces:
            list.addWidget(FaceEmotion(face))

        widget = QWidget()
        widget.setLayout(list)

        scrollArea = QScrollArea()
        scrollArea.setWidget(widget)

        self.mylayout = QVBoxLayout()
        self.mylayout.addWidget(QLabel("Emotions:"))
        self.mylayout.addWidget(scrollArea)
        self.setLayout(self.mylayout)
        self.setFixedWidth(600)

class MainWindow(QMainWindow):

   

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setFixedSize(1400,1000)
        self.setWindowTitle("Emotion recognizer")

        self.placeHolder = QLabel()
        self.placeHolder.setFixedSize(800,400)

        self.img_before = self.placeHolder
        self.img_after = self.placeHolder
        
        self.render()

        menu_bar = self.menuBar()
        load_action = menu_bar.addAction("&Load")
        load_action.triggered.connect(self.load)
        load_action = menu_bar.addAction("&Recognize")
        load_action.triggered.connect(self.recognize)
        quit_action = menu_bar.addAction("&Quit")
        quit_action.triggered.connect(lambda: self.app.quit())
    
    def load(self):
        self.img_before = displayImageWidget()
        self.render()

    def recognize(self):
        self.img_after = displayImageWidget()
        self.render()
        

    def render(self):
        v_layout2 = QVBoxLayout()
    
        h_layout = QHBoxLayout()
        h_layout.addWidget(Images_VLayoutWidget(self.img_before,self.img_after))
        h_layout.addWidget(Scroll_VLayoutWidget(range(0,10)))

        central = QWidget()
        central.setLayout(h_layout)
        self.setCentralWidget(central)

