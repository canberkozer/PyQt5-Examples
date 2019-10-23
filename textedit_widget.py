from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QFont

font = QFont("Arial",14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,300,300)
        self.setWindowTitle("Using Text Edit")
        self.UI()
    
    def UI(self):
        self.editor =QTextEdit(self)
        self.editor.move (50,50)
        button = QPushButton("send",self)
        self.editor.setAcceptRichText(False)
        button.move(150,280)
        button.clicked.connect(self.getValue)
        self.show()
    def getValue(self):
        print(self.editor.toPlainText())

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()