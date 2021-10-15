from os import stat
from src.model.board import Board
from src.model.player import Player
from src.model.state import State
from src.constant import GameConstant

class Test3:
    def __init__(self, config):
        board = Board(config.row, config.col)
        players = [
            Player(
                GameConstant.PLAYER1_SHAPE, GameConstant.PLAYER1_COLOR, config.quota[0]
            ),
            Player(
                GameConstant.PLAYER2_SHAPE, GameConstant.PLAYER2_COLOR, config.quota[1]
            ),
        ]

        self.__gen_player()
        self.state = State(board, players, 1)

        self.state.__str__()

