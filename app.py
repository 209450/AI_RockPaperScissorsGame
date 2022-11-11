import sys

import cv2
from PyQt5.QtWidgets import QApplication

from GUI.MainWindow import MainWindow
from GUI.MainWindowController import MainWindowController
from GUI.RockPaperScissorsGame import RockPaperScissorsGame


class App(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        model = RockPaperScissorsGame()
        controller = MainWindowController(model)
        main_window = MainWindow(model, controller)
        main_window.show()
        self.main_window = main_window


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())
