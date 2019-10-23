from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QFont

font = QFont("Arial",14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,300,300)
        self.setWindowTitle("Using Spinbox")
        self.UI()
    
    def UI(self):
        self.spinbox = QSpinBox(self)
        self.spinbox.move(100,100)
        self.spinbox.setFont(font)
        self.spinbox.setMinimum(25)
        self.spinbox.setMaximum(50)
        #self.spinbox.setRange(25,50)
        self.spinbox.setPrefix("$")
        self.spinbox.setSuffix(" per hour")
        self.spinbox.setSingleStep(5)
        #self.spinbox.valueChanged.connect(self.getValue)
        button = QPushButton("Send",self)
        button.move(100,130)
        button.clicked.connect(self.getValue)
        self.show()

    def getValue(self):
        print(f"Value: {self.spinbox.value()}")
        

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()