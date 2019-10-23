from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,300,300)
        self.setWindowTitle("Using Labels")
        self.UI()
    
    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter your name")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter your surname")
        self.name.move(150,50)
        self.surname.move(150,80)
        self.remember = QCheckBox("Remember me",self)
        self.remember.move(150,110)
        button = QPushButton("Submit",self)
        button.move(200,140)
        button.clicked.connect(self.submit)
        self.show()
    
    def submit(self):
        if(self.remember.isChecked()):
            print(f"Name: {self.name.text()} Surname: {self.surname.text()} Remember me button is checked")
        else:
            print(f"Name: {self.name.text()} Surname: {self.surname.text()} Remember me button is not checked")
            
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()