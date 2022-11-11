import random
from enum import Enum, auto

from PyQt5.QtCore import pyqtSignal, QObject

from GUI.ConfigParserFactory import ConfigParserFactory


class RockPaperScissorsGame(QObject):
    change_player_label = pyqtSignal(str)
    change_enemy_label = pyqtSignal(str)
    update_game_log = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.game_state = GameState()
        self.config_parser = ConfigParserFactory.load_config_parser()
        self.images = {GameMoves.ROCK: self.config_parser["Game"]["rock_image"],
                       GameMoves.PAPER: self.config_parser["Game"]["paper_image"],
                       GameMoves.SCISSORS: self.config_parser["Game"]["scissors_image"]}

    def play(self, player_move):
        player_score, enemy_score = self.game_state.player_score, self.game_state.enemy_score
        enemy_move = self.make_enemy_move()

        # player is a winner
        if (player_move is GameMoves.ROCK and enemy_move is GameMoves.SCISSORS) \
                or (player_move is GameMoves.PAPER and enemy_move is GameMoves.ROCK) \
                or (player_move is GameMoves.SCISSORS and enemy_move is GameMoves.PAPER):
            player_score += 1
            enemy_score -= 1
        # withdraw
        elif player_move is enemy_move:
            pass
        # enemy is a winner
        else:
            player_score -= 1
            enemy_score += 1

        self.game_state = GameState(player_score, enemy_score, player_move, enemy_move)
        self.update_view()

    def make_enemy_move(self):
        return random.choice(list(GameMoves))

    def update_view(self):
        game_state = self.game_state

        self.change_player_label.emit(self.images[game_state.player_move])
        self.change_enemy_label.emit(self.images[game_state.enemy_move])
        self.update_game_log.emit(str(game_state.__dict__))


class GameState:
    def __init__(self, player_score=0, enemy_score=0, player_move=None, enemy_move=None):
        self.player_score = player_score
        self.enemy_score = enemy_score
        self.player_move = player_move
        self.enemy_move = enemy_move


class GameMoves(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()
