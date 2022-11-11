from AI.RockPaperScissorsClassifier import RockPaperScissorsClassifier
from GUI.CameraReceiver import CameraReceiver
from GUI.ConfigParserFactory import ConfigParserFactory
from GUI.RockPaperScissorsGame import GameMoves


class MainWindowController:

    def __init__(self, model):
        self.model = model
        self.camera = CameraReceiver()
        self.classifier = RockPaperScissorsClassifier()
        self.config_parser = ConfigParserFactory.load_config_parser()

        camera_url = self.config_parser["Camera"]["url"]
        self.camera.connect_to_url_camera(camera_url)
        network_path = self.config_parser["Network"]["model_path"]
        self.classifier.load_model(network_path)

        self.labels_moves = {"rock": GameMoves.ROCK,
                             "paper": GameMoves.PAPER,
                             "scissors": GameMoves.SCISSORS}

    def play_game_with_video(self, frame):
        image = self.classifier.reshape_image(frame)
        prediction = self.classifier.predict(image)
        self.model.play(self.labels_moves[prediction])
