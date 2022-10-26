#!/usr/bin/python3
import time

timeLeft = input('How long would you like the timer to be?: ')
timeLeft = int(timeLeft)

print(timeLeft)
for i in range(timeLeft - 1, -1, -1):
    time.sleep(1)
    print(str(i))

print("TIME UP!")