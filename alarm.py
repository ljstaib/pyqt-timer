#!/usr/bin/python3

"""
Python Study Timer

Simple timer program created in Python.

Author: Luke Staib
"""

import sys
import datetime
from playsound import playsound

from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QDialog, QMenu
from PyQt6.QtCore import QFile, QTimer, Qt, QTextStream
from PyQt6.QtGui import QFont, QIntValidator, QAction

def _changeStyle(path):
    app = QApplication.instance()
    if app is None:
        return

    print(path)
    with open(path, 'r') as f:
        style = f.read()
        app.setStyleSheet(style)

class TimeDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setWindowTitle('Set Time')
        self.setGeometry(100, 100, 170, 200)
        self.parent = parent
        self._getUI()
    
    def _getUI(self):
        self.hoursLabel = QLabel(self)
        self.hoursLabel.setText('   Hours (0-99):')
        self.hoursLabel.setGeometry(0, 0, 200, 50)

        # Check input so hours can only be 0-99, minutes: 0-59, seconds: 0-59
        self.hoursIn = QLineEdit(self)
        self.hoursIn.move(115, 15)
        self.hoursIn.resize(50, 20)

        hoursValidator = QIntValidator(0, 99, self)
        self.hoursIn.setValidator(hoursValidator)
        self.hoursIn.setMaxLength(2)

        self.minutesLabel = QLabel(self)
        self.minutesLabel.setText('   Minutes (0-59):')
        self.minutesLabel.setGeometry(0, 35, 200, 50)

        self.minutesIn = QLineEdit(self)
        self.minutesIn.move(115, 50)
        self.minutesIn.resize(50, 20)
        
        minsecValidator = QIntValidator(0, 59, self)
        self.minutesIn.setValidator(minsecValidator)
        self.minutesIn.setMaxLength(2)

        self.secondsLabel = QLabel(self)
        self.secondsLabel.setText('   Seconds (0-59):')
        self.secondsLabel.setGeometry(0, 70, 200, 50)

        self.secondsIn = QLineEdit(self)
        self.secondsIn.move(115, 85)
        self.secondsIn.resize(50, 20)
        self.secondsIn.setValidator(minsecValidator)
        self.secondsIn.setMaxLength(2)

        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.setGeometry(15, 150, 60, 30)
        self.cancelButton.clicked.connect(self._cancelInfo)

        self.okButton = QPushButton('OK', self)
        self.okButton.setGeometry(100, 150, 60, 30)
        self.okButton.clicked.connect(self._sendInfo)

        self.errorLabel = QLabel(self)
        self.errorLabel.setText("")
        self.errorLabel.setFont(QFont('Arial', 12))
        self.errorLabel.setGeometry(0, 110, 200, 30)

    def _clearInputs(self):
        # Clear inputs and hide error text if it was there
        self.errorLabel.setText("")
        self.hoursIn.setText("")
        self.minutesIn.setText("")
        self.secondsIn.setText("")

    def _cancelInfo(self):
        self._clearInputs()
        self.close()

    def _sendInfo(self):
        # Retrieve number of hours, minutes, and seconds inputted and init timer

        if self.hoursIn.text() == "" or self.minutesIn.text() == "" or self.secondsIn.text() == "":
            self.errorLabel.setText('  ERROR: Value/s out of range.')
        else:
            if int(self.minutesIn.text()) <= 59 and int(self.secondsIn.text()) <= 59:
                # Gather input from user
                self.parent.hours = self.hoursIn.text()
                self.parent.minutes = self.minutesIn.text()
                self.parent.seconds = self.secondsIn.text()

                # Send data to main window
                self.parent._initTimerValues()

                self._clearInputs()

                # Close window
                self.close()  
            else:
                # Show error text
                self.errorLabel.setText('  ERROR: Value/s out of range.')


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self.setWindowTitle('Study Timer')
        # self.setGeometry(100, 100, 300, 180)
        self.setFixedSize(300, 180)
        self.timeDialog = TimeDialog(self)
        self._getMenuBar()
        self._getUI()

    def _getMenuBar(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)

        timeMenuAction = QAction('&Set Time', self)
        timeMenuAction.triggered.connect(self._getTime)
        menuBar.addAction(timeMenuAction)

        settingsMenu = QMenu("&Settings", self)
        menuBar.addMenu(settingsMenu)

        themesMenu = QMenu('&Themes', self)
        lightAction = QAction('&Light', self)
        lightAction.triggered.connect(lambda: _changeStyle("assets/stylesheets/light.qss"))
        darkAction = QAction('&Dark', self)
        darkAction.triggered.connect(lambda: _changeStyle("assets/stylesheets/dark.qss"))
        themesMenu.addAction(lightAction)
        themesMenu.addAction(darkAction)
        settingsMenu.addMenu(themesMenu)
    
    def _getUI(self):
        # Variables
        self.count, self.start = 0, False
        self.hours, self.minutes, self.seconds = 0, 0, 0
        self.lastVal = 0

        # Create button to set the length of the timer: made obsolete by menu button
        # self.setTimeButton = QPushButton('Set time', self)
        # self.setTimeButton.setGeometry(125, 100, 150, 50)
        # self.setTimeButton.clicked.connect(self._getTime)

        # Create label to show time left
        self.label = QLabel("00:00:00", self)
        self.label.setGeometry(0, 30, 300, 100)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Formal time label
        self.label.setFont(QFont('Helvetica', 64))

        # Create start button
        self.startButton = QPushButton("Start", self)
        self.startButton.setGeometry(15, 130, 60, 40)
        self.startButton.clicked.connect(self._startTimer)

        # Create pause button
        self.pauseButton = QPushButton("Pause", self)
        self.pauseButton.setGeometry(85, 130, 60, 40)
        self.pauseButton.clicked.connect(self._pauseTimer)

        # Create restart button
        self.restartButton = QPushButton("Restart", self)
        self.restartButton.setGeometry(155, 130, 60, 40)
        self.restartButton.clicked.connect(self._restartTimer)

        # Create reset button
        self.resetButton = QPushButton("Reset", self)
        self.resetButton.setGeometry(225, 130, 60, 40)
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
                # Sound alarm!
                playsound('assets/sound/alarm.wav')
        
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
    _changeStyle("assets/stylesheets/light.qss")
    sys.exit(app.exec())