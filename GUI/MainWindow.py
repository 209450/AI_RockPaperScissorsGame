import cv2
from PyQt5 import uic
from PyQt5.QtCore import QThread, QRunnable, QThreadPool, QTimer, pyqtSlot, pyqtSignal, QSize
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow

from GUI.ConfigParserFactory import ConfigParserFactory


class MainWindow(QMainWindow):

    def __init__(self, model, controller):
        super().__init__()
        self.model = model
        self.controller = controller
        self.config_parser = ConfigParserFactory.load_config_parser()
        uic.loadUi(self.config_parser["MainWindow"]["ui_path"], self)

        main_window_parser = self.config_parser["MainWindow"]
        self.image_size = QSize(int(main_window_parser["img_width"]), int(main_window_parser["img_height"]))

        self.playPushButton.clicked.connect(self.play_button_handler)
        self.model.change_player_label.connect(self.update_player_label)
        self.model.change_enemy_label.connect(self.update_enemy_label)
        self.model.update_game_log.connect(self.update_game_log)

        self.streamable_window_thread = StreamableWindow(self.controller.camera)
        self.streamable_window_thread.start()

    def play_button_handler(self):
        self.controller.play_game_with_video(self.streamable_window_thread.current_frame)

    @pyqtSlot(str)
    def update_player_label(self, img_path):
        self._update_label_from_file(self.playerLabel, img_path)

    @pyqtSlot(str)
    def update_enemy_label(self, img_path):
        self._update_label_from_file(self.enemyLabel, img_path)

    @pyqtSlot(str)
    def update_game_log(self, str_update):
        self.gameLog.append(str_update)

    def _update_label_from_file(self, label, img_path):
        image = QImage(img_path)
        image = image.scaled(self.image_size)
        label.setPixmap(QPixmap(image))


class StreamableWindow(QThread):

    def __init__(self, camera):
        super().__init__()
        self.camera = camera
        self.current_frame = None

    def run(self):
        while True:
            frame = self.camera.retrieve_video_frame()
            self.current_frame = frame

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
