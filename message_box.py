from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QFont

font = QFont("Arial",14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,300,300)
        self.setWindowTitle("Using Message Boxes")
        self.UI()
    
    def UI(self):
        button = QPushButton("Click Me",self)
        button.move(100,100)
        button.setFont(font)
        button.clicked.connect(self.messageBox)
        self.show()
    def messageBox(self):
        mbox = QMessageBox.information(self,"Information!!","Are you sure to exit?")
        #mbox1 = QMessageBox.question(self,"Warning!!","Are you sure to exit?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()
        elif mbox == QMessageBox.No:
            print("You clicked No Button")
        

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()