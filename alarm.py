#!/usr/bin/python3

import sys
import datetime

from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QDialog
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont

class TimeDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setWindowTitle('Set Time')
        self.setGeometry(100, 100, 300, 150)
        self.parent = parent
        self._getUI()
    
    def _getUI(self):
        self.hoursLabel = QLabel(self)
        self.hoursLabel.setText('Hours:')
        self.hoursLabel.setGeometry(25, 0, 200, 50)

        self.hoursIn = QLineEdit(self)
        self.hoursIn.move(85, 15)
        self.hoursIn.resize(200, 20)

        self.minutesLabel = QLabel(self)
        self.minutesLabel.setText('Minutes:')
        self.minutesLabel.setGeometry(25, 30, 200, 50)

        self.minutesIn = QLineEdit(self)
        self.minutesIn.move(85, 45)
        self.minutesIn.resize(200, 20)

        self.secondsLabel = QLabel(self)
        self.secondsLabel.setText('Seconds:')
        self.secondsLabel.setGeometry(25, 60, 200, 50)

        self.secondsIn = QLineEdit(self)
        self.secondsIn.move(85, 75)
        self.secondsIn.resize(200, 20)

        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.setGeometry(75, 105, 80, 40)
        self.cancelButton.clicked.connect(self.close)

        self.okButton = QPushButton('OK', self)
        self.okButton.setGeometry(175, 105, 80, 40)
        self.okButton.clicked.connect(self._sendInfo)

    def _sendInfo(self):
        # Retrieve number of hours, minutes, and seconds inputted and init timer

        # TODO: Check input so hours can only be 0-99, minutes: 0-59, seconds: 0-59
        self.parent.hours = self.hoursIn.text()
        self.parent.minutes = self.minutesIn.text()
        self.parent.seconds = self.secondsIn.text()

        self.parent._initTimerValues()

        self.close()


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self.setWindowTitle('Study Timer')
        self.setGeometry(100, 100, 400, 600)
        self.timeDialog = TimeDialog(self)
        self._getUI()
    
    def _getUI(self):
        # Variables
        self.count, self.start = 0, False
        self.hours, self.minutes, self.seconds = 0, 0, 0
        self.lastVal = 0

        # Create button to set the length of the timer
        self.setTimeButton = QPushButton('Set time', self)
        self.setTimeButton.setGeometry(125, 100, 150, 50)
        self.setTimeButton.clicked.connect(self._getTime)

        # Create label to show time left
        self.label = QLabel("00:00:00", self)
        self.label.setGeometry(50, 200, 300, 100)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Formal time label
        self.label.setFont(QFont('Helvetica', 64))

        # Create start button
        self.startButton = QPushButton("Start", self)
        self.startButton.setGeometry(125, 350, 150, 40)
        self.startButton.clicked.connect(self._startTimer)

        # Create pause button
        self.pauseButton = QPushButton("Pause", self)
        self.pauseButton.setGeometry(125, 400, 150, 40)
        self.pauseButton.clicked.connect(self._pauseTimer)

        # Create restart button
        self.restartButton = QPushButton("Restart", self)
        self.restartButton.setGeometry(125, 450, 150, 40)
        self.restartButton.clicked.connect(self._restartTimer)

        # Create reset button
        self.resetButton = QPushButton("Reset", self)
        self.resetButton.setGeometry(125, 500, 150, 40)
        self.resetButton.clicked.connect(self._resetTimer)

        # Create test button
        # self.resetButton = QPushButton("Test", self)
        # self.resetButton.setGeometry(125, 550, 150, 40)
        # self.resetButton.clicked.connect(self._testValues)

        # Create timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._showTimer)
        self.timer.start(100)

    def _getTime(self):
        # Triggered when "Set time" button pressed
        self.start = False

        # Init other window
        self.timeDialog.show()

    def _initTimerValues(self):
        # Get total seconds from "set time" dialog
        totalTime = int(self.hours) * 3600 + int(self.minutes) * 60 + int(self.seconds)
        self.count = totalTime * 10
        self.lastVal = self.count / 10

        self._setTimer(self.lastVal)

    def _startTimer(self):
        # Start timer
        self.start = True

        if self.count == 0:
            self.start = False
    
    def _pauseTimer(self):
        # Pause timer
        self.start = False

    def _restartTimer(self):
        # Restart timer using last used hours, minutes, seconds values
        self.count, self.start = self.lastVal * 10, False
        self._setTimer(self.lastVal)

    def _resetTimer(self):
        # Reset timer and all values
        self.count, self.start, self.lastVal = 0, False, 0
        self.hours, self.minutes, self.seconds = 0, 0, 0
        self.label.setText("00:00:00")

    def _testValues(self):
        # Debug function
        print(self.hours, self.minutes, self.seconds)

    def _showTimer(self):
        # Used to update timer
        if self.start:
            self.count -= 1

            if self.count == 0:
                self.start = False
                self.label.setText("00:00:00")
                # TODO: Sound alarm!
        
        if self.start:
            self._setTimer(self.count / 10)
    
    def _setTimer(self, secs_in):
        # Used to format timer
        dt_curr = datetime.timedelta(seconds=round(secs_in))
        dt_curr = int(dt_curr.total_seconds())
        self.label.setText('{:02}:{:02}:{:02}'.format(dt_curr // 3600, dt_curr % 3600 // 60, dt_curr % 60))

if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())