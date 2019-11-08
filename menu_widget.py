from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,600,600)
        self.setWindowTitle("Menu Widget")
        self.UI()
    
    def UI(self):
        #Main Menu
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        helpMenu = menubar.addMenu("Help")

        #Sub Menu
        new = QAction("New Project",self)
        new.setShortcut("Ctrl+O")
        file.addAction(new)
        open_ = QAction("Open",self)
        file.addAction(open_)
        exit = QAction("Exit",self)
        file.addAction(exit)
        exit.setIcon(QIcon("assets/rock.png"))
        exit.triggered.connect(self.exitFunc)

        #Toolbar
        tb = self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        newTb = QAction(QIcon("assets/scissors.png"),"New",self)
        tb.addAction(newTb)
        openTb = QAction(QIcon("assets/paper.png"),"Open",self)
        tb.addAction(openTb)
        saveTb = QAction(QIcon("assets/rock.png"),"Save",self)
        tb.addAction(saveTb)
        saveTb.triggered.connect(self.exitFunc)
        tb.actionTriggered.connect(self.btnFunc)

        self.combo = QComboBox()
        self.combo.addItems(["X","W","Z"])
        tb.addWidget(self.combo)

        self.show()

    def btnFunc(self,btn):
        if btn.text() == "New":
            print("You clicked new button")
        elif btn.text() == "Open":
            print("You clicked open button")
        else:
            print("You clicked save button")

    def exitFunc(self):
        mbox = QMessageBox.information(self,"Warning","Are you sure to exit?",QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()