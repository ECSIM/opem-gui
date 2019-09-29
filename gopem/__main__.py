"""GOPEM main."""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from art import tprint
from gopem.mainwindow import MainWindow
from gopem.helper import Version,CiteMessage
import sys

if __name__ == "__main__":
    tprint("GOPEM")
    tprint("v" + str(Version))
    try:
        QtCore.Qt.AA_EnableHighDpiScaling = 1
    except Exception as e:
        print(str(e))
    app = QApplication(sys.argv)
    a = MainWindow()
    a.location_on_screen()
    if len(sys.argv) > 1 and sys.argv[1] == "--test" and app is not None:
        sys.exit(0)
    a.show()
    a.message_box("Welcome",CiteMessage)
    if app is not None:
        sys.exit(app.exec_())
