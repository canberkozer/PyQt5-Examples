#Rock Paper Scissors Game
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

textFont = QFont("Times",14)
buttonFont = QFont("Arial",12)
computerScore = 0
playerScore = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,350,550,250)
        self.setWindowTitle("Rock Paper Scissors")
        self.UI()
    
    def UI(self):
        self.scoreComputerText=QLabel("Computer Score: ",self)
        self.scoreComputerText.move(30,20)
        self.scoreComputerText.setFont(textFont)
        self.scorePlayerText=QLabel("Player Score: ",self)
        self.scorePlayerText.move(330,20)
        self.scorePlayerText.setFont(textFont)

        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap("assets/rock.png"))
        self.imageComputer.move(50,40)
        self.imageComputer.resize(100,100)

        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("assets/rock.png"))
        self.imagePlayer.move(330,40)
        self.imagePlayer.resize(100,100)

        btnStart = QPushButton("Start",self)
        btnStop = QPushButton("Stop",self)
        btnStart.setFont(buttonFont)
        btnStop.setFont(buttonFont)
        btnStart.move(50,150)
        btnStop.move(330,150)
        btnStart.clicked.connect(self.start)
        btnStop.clicked.connect(self.stop)

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.playGame)

        self.show()
    
    def playGame(self):
        self.rndComputer = randint(1,3)
        if self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap("assets/rock.png"))
        elif self.rndComputer == 2:
            self.imageComputer.setPixmap(QPixmap("assets/paper.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("assets/scissors.png"))

        self.rndPlayer = randint(1,3)
        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("assets/rock.png"))
        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("assets/paper.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("assets/scissors.png")) 
        
    def start(self):
        self.timer.start()
    def stop(self):
        self.timer.stop()
        global computerScore
        global playerScore

        if self.rndComputer == 1 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self,"Information","Draw Game")

        elif self.rndComputer == 1 and self.rndPlayer ==2:
            mbox = QMessageBox.information(self,"Information","You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score: {}".format(playerScore))

        elif self.rndComputer == 1 and self.rndPlayer ==3:
            mbox = QMessageBox.information(self,"Information","Computer Win")
            computerScore += 1
            self.scoreComputerText.setText("Computer Score: {}".format(computerScore))

        elif self.rndComputer ==2 and self.rndPlayer==1:
            mbox = QMessageBox.information(self,"Information","Computer Win")
            computerScore += 1
            self.scoreComputerText.setText("Computer Score: {}".format(computerScore))

        elif self.rndComputer ==2 and self.rndPlayer ==2:
            mbox = QMessageBox.information(self,"Information","Draw Game")

        elif self.rndComputer ==2 and self.rndPlayer==3:
            mbox = QMessageBox.information(self,"Information","You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score: {}".format(playerScore))

        elif self.rndComputer ==3 and self.rndPlayer ==1:
            mbox = QMessageBox.information(self,"Information","You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score: {}".format(playerScore))

        elif self.rndComputer ==3 and self.rndPlayer ==2:
            mbox = QMessageBox.information(self,"Information","Computer Win")
            computerScore += 1
            self.scoreComputerText.setText("Computer Score: {}".format(computerScore))

        elif self.rndComputer ==3 and self.rndPlayer ==3:
            mbox = QMessageBox.information(self,"Information","Draw Game")

        if computerScore == 3 or playerScore == 3:
            mbox=QMessageBox.information(self,"Information","Game Over")
            sys.exit()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()