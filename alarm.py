#!/usr/bin/python3

import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QInputDialog
from PyQt6.QtCore import QTimer

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self.setWindowTitle('Study Timer')
        self.setGeometry(100, 100, 400, 600)
        self._getUI()
    
    def _getUI(self):
        # Variables
        self.count, self.start = 0, False

        # Create button to set the length of the timer
        self.setTimeButton = QPushButton('Set time', self)
        self.setTimeButton.setGeometry(125, 100, 150, 50)
        self.setTimeButton.clicked.connect(self._getTime)

        # Create label to show time left
        self.label = QLabel("//TIMER//", self)
        self.label.setGeometry(100, 200, 200, 50)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Create start button
        self.startButton = QPushButton("Start", self)
        self.startButton.setGeometry(125, 350, 150, 40)
        self.startButton.clicked.connect(self._startTimer)

        # Create pause button
        self.pauseButton = QPushButton("Pause", self)
        self.pauseButton.setGeometry(125, 400, 150, 40)
        self.pauseButton.clicked.connect(self._pauseTimer)

        # Create reset button
        self.resetButton = QPushButton("Reset", self)
        self.resetButton.setGeometry(125, 450, 150, 40)
        self.resetButton.clicked.connect(self._resetTimer)

        # Create timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._showTimer)
        self.timer.start(100)

    def _getTime(self):
        self.start = False

        seconds_in, isDone = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')

        # Retrieve number of seconds inputted and init timer
        if isDone:
            self.count = seconds_in * 10
            self.label.setText(str(seconds_in))


    def _startTimer(self):
        self.start = True

        if self.count == 0:
            self.start = False
    
    def _pauseTimer(self):
        self.start = False

    def _resetTimer(self):
        self.count, self.start = 0, False
        self.label.setText("//TIMER//")

    def _showTimer(self):
        if self.start:
            self.count -= 1

            if self.count == 0:
                self.start = False
                self.label.setText("Timer Done.")
        
        if self.start:
            self.label.setText(str(self.count / 10))

if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())