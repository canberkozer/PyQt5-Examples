from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,300,300)
        self.setWindowTitle("Using Timer")
        self.UI()
    
    def UI(self):
        self.colorLabel = QLabel(self)
        self.colorLabel.resize(250,250)
        self.colorLabel.move(20,20)
        self.colorLabel.setStyleSheet("background-color:black")
        btnStart = QPushButton("Start",self)
        btnStart.move(70,270)
        btnStop = QPushButton("Stop",self)
        btnStop.move(140,270)
        btnStart.clicked.connect(self.start)
        btnStop.clicked.connect(self.stop)

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.changeColor)
        self.value = 0

        self.show()
    def changeColor(self):
        if self.value==0:
            self.colorLabel.setStyleSheet("background-color:yellow")
            self.value = 1
        else:
            self.colorLabel.setStyleSheet("background-color:black")
            self.value = 0
    def start(self):
        self.timer.start()
    def stop(self):
        self.timer.stop()
def main():
    App = QApplication(sys.argv)
    window = Window()
    window.start()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()