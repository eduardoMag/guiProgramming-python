import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *


app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = "Alert!"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
except ValueError:
    message = "usage: alert.pyw HH:MM [optional message]"
    while QTime.currentTime() < due:
        time.sleep(20) #20 seconds
