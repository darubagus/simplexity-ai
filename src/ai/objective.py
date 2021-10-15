import pickle
from typing import Tuple
from src.model import Player
from src.model import Piece, Board, State
from src.constant import ShapeConstant, GameConstant, ColorConstant
from src.matrixProc import *

#INI BUAT TESTING
board = Board(6, 7)
        
def objective(_state : State):
    """
    
    """
    player = _state.players
    arrays = []
    states = {}

    player = _state.players[(_state.round - 1) % 2]
    board = np.array(_state.board.board)
    arrays += runSplitHV(board)
    arrays += runSplitDiagonal(board)

    for window in arrays:
        checkWindow(window, states)
    
    return countStateValue(states, player)

def checkWindow(_window, _states):
    colors = ["BLUE", "RED", "BLACK"]
    shapes = ["X", "O", "-"]
    for color in colors:
        counter = 0
        for cell in _window:
            if (cell.color == color):
                counter += 1
        if (color+str(counter)) not in _states:
            _states[color+str(counter)] = 0
        # print(color+str(counter))
        _states[color+str(counter)] += 1

    for shape in shapes:
        counter = 0
        for cell in _window:
            if (cell.shape == shape):
                counter += 1
        if (shape+str(counter)) not in _states:
            _states[shape+str(counter)] = 0
        _states[shape+str(counter)] += 1
    # print(_states)

def countStateValue(_state, _player):
    valid_colors = ["BLUE", "RED"]
    valid_shapes = ["X", "O"]
    weights = {
        "SHAPE1":1,
        "SHAPE2":2,
        "SHAPE3":3,
        "COLOR1":0.5,
        "COLOR2":1.5,
        "COLOR3":2.5 }
    player_shape = _player.shape
    player_color = _player.color
    total = 0
    
    for key in _state:
        if (key[:-1] in valid_colors and key[-1] != "0"):
            cweight = str(key[-1])
            weight_key = "COLOR" + cweight

            if (player_color == "BLUE"):
                if ("BLUE" + cweight) not in _state:
                    total += weights[weight_key] * (0 - _state["RED" + cweight])
                elif ("RED" + cweight) not in _state:
                    total += weights[weight_key] * (_state["BLUE" + cweight])
                else: 
                    total += weights[weight_key] * (_state["BLUE" + cweight] - _state["RED" + cweight])
            else:
                if ("RED" + cweight) not in _state:
                    total += weights[weight_key] * (0 - _state["BLUE" + cweight])
                elif ("BLUE" + cweight) not in _state:
                    total += weights[weight_key] * (_state["RED" + cweight])
                else:
                    total += weights[weight_key] * (_state["RED" + cweight] - _state["BLUE" + cweight])

        if (key[:-1] in valid_shapes and key[-1] != "0"):
            cweight = str(key[-1])
            weight_key = "SHAPE" + cweight

            if (player_shape == "X"):
                if ("X" + cweight) not in _state:
                    total += weights[weight_key] * (0 - _state["O" + cweight])
                elif ("O" + cweight) not in _state:
                    total += weights[weight_key] * (_state["X" + cweight])
                else: 
                    total += weights[weight_key] * (_state["X" + cweight] - _state["O" + cweight])
            else:
                if ("O" + cweight) not in _state:
                    total += weights[weight_key] * (0 - _state["X" + cweight])
                elif ("X" + cweight) not in _state:
                    total += weights[weight_key] * (_state["O" + cweight])
                else:
                    total += weights[weight_key] * (_state["O" + cweight] - _state["X" + cweight])
    print(_state)
    return total
    
# print(np.array(board))

