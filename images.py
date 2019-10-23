from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,350,350)
        self.setWindowTitle("Using Labels")
        self.UI()
    
    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('assets/logo.png'))
        self.image.move(50,20)

        removeButton = QPushButton("Remove",self)
        showButton = QPushButton("Show",self)
        removeButton.move(80,280)
        showButton.move(180,280)
        removeButton.clicked.connect(self.removeImg)
        showButton.clicked.connect(self.showImg)
        self.show()

    def removeImg(self):
        self.image.close()
    def showImg(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()