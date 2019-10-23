from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,300,300)
        self.setWindowTitle("Using Combo Box")
        self.UI()
    
    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150,100)
        button = QPushButton("Save",self)
        button.move(150,130)
        button.clicked.connect(self.getValue)
        self.combo.addItem("Python")
        self.combo.addItems(["C","C#","C++"])
        self.show()
    def getValue(self):
        value = self.combo.currentText()
        print(value)
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()