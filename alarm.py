#!/usr/bin/python3

import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QInputDialog
from PyQt6.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Study Timer')
        self.setGeometry(100, 100, 400, 600)
        self.getUI()
    
    def getUI(self):
        # Variables
        self.count, self.start = 0, False

        # Create button to set the length of the timer
        self.setTimeButton = QPushButton('Set time')
        self.setTimeButton.setGeometry(125, 100, 150, 50)
        self.setTimeButton.clicked.connect(self.getTime)

        # Create label to show time left
        self.label = QLabel("//TIMER//")
        self.label.setGeometry(100, 200, 200, 50)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Create start button
        self.startButton = QPushButton("Start")
        self.startButton.setGeometry(125, 350, 150, 40)
        self.startButton.clicked.connect(self.startTimer)

        # Create pause button
        self.pauseButton = QPushButton("Pause")
        self.pauseButton.setGeometry(125, 400, 150, 40)
        self.pauseButton.clicked.connect(self.pauseTimer)

        # Create reset button
        self.resetButton = QPushButton("Reset")
        self.resetButton.setGeometry(125, 450, 150, 40)
        self.resetButton.clicked.connect(self.resetTimer)

        # Create timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTimer)
        self.timer.start(100)

    def getTime(self):
        self.start = False

        seconds_in, isDone = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')

        # Retrieve number of seconds inputted and init timer
        if isDone:
            self.count = seconds_in * 10
            self.label.setText(str(seconds_in))


    def startTimer(self):
        self.start = True

        if self.count == 0:
            self.start = False
    
    def pauseTimer(self):
        self.start = False

    def resetTimer(self):
        self.count, self.start = 0, False
        self.label.setText("//TIMER//")

    def showTimer(self):
        if self.start:
            self.count -= 1

            if self.count == 0:
                self.start = False
                self.label.setText("Timer Done.")
        
        if self.start:
            self.label.setText(str(self.count / 10))

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())