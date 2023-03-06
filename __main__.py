from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QHBoxLayout, QGridLayout
from mainwindow import MainWindow
import sys      

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow(app)
    main_window.show()
    sys.exit(app.exec())
