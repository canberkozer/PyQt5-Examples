from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,300,500,500)
        self.setWindowTitle("Using List Widget")
        self.UI()
    
    def UI(self):
        self.addRecord=QLineEdit(self)
        self.addRecord.move(50,50)
        self.listWidget = QListWidget(self)
        self.listWidget.move(50,80)
        btnAdd = QPushButton("Add",self)
        btnDelete = QPushButton("Delete",self)
        btnGet = QPushButton("Get",self)
        btnDeleteAll = QPushButton("Delete All",self)
        btnAdd.move(50,300)
        btnDelete.move(130,300)
        btnGet.move(210,300)
        btnDeleteAll.move(290,300)
        btnAdd.clicked.connect(self.funcAdd)
        btnDelete.clicked.connect(self.funcDelete)
        btnGet.clicked.connect(self.funcGet)
        btnDeleteAll.clicked.connect(self.funcDeleteAll)

        self.show()
    def funcAdd(self):
        value = self.addRecord.text()
        self.listWidget.addItem(value)
        self.addRecord.setText("")
    def funcDelete(self):
        value = self.listWidget.currentRow()
        self.listWidget.takeItem(value)
    def funcGet(self):
        value = self.listWidget.currentItem().text()
        print(value)
    def funcDeleteAll(self):
        self.listWidget.clear()
    
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()