from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,300,300)
        self.setWindowTitle("Using Radio Buttons")
        self.UI()
    
    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter your name")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter your surname")
        self.name.move(100,50)
        self.surname.move(100,80)
        self.male = QRadioButton("male",self)
        self.male.move(100,110)
        self.female = QRadioButton("female",self)
        self.female.move(100,130)
        button = QPushButton("Submit",self)
        button.move(150,150)
        button.clicked.connect(self.submit)
        self.show()
    def submit(self):
        if(self.male.isChecked()):
            print(f"Name: {self.name.text()}, Surname: {self.name.text()}, Gender: Male")
        else:
            print(f"Name: {self.name.text()}, Surname: {self.name.text()}, Gender: Female")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()