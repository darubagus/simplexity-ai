import pickle
import timeit
import numpy as np
from typing import Tuple
from src.model import Player
from src.model import Piece, Board, State
from src.constant import ShapeConstant, GameConstant, ColorConstant
# from src.matrixProc import *

#INI BUAT TESTING
board = Board(6, 7)
        
def objective(_state : State, n_player: int):
    """
    
    """
    player = _state.players
    arrays = []
    states = {}

    player = _state.players[n_player]

    board = np.array(_state.board.board)
    arrays += runSplitHV(board)
    arrays += runSplitDiagonal(board)
 
    # print(len(arrays))
    
    for window in arrays:
        checkWindow(window, states)

    return countStateValue(states, player)

def checkWindow(_window, _states):
    # start = timeit.default_timer()

    # global ctr
    # ctr +=1
    
    colors = ["BLUE", "RED", "BLACK"]
    shapes = ["X", "O", "-"]
    for color in colors:
        counter = 0
        counter_blank = 0
        for cell in _window:
            if (cell.color == color and cell.color != "BLACK"):
                counter += 1
            if (cell.color == "BLACK"):
                counter_blank += 1
        if (color+str(counter)) not in _states:
            _states[color+str(counter)] = 0
        if (counter + counter_blank == 4):
            _states[color+str(counter)] += 1

    for shape in shapes:
        counter = 0
        counter_blank = 0
        for cell in _window:
            if (cell.shape == shape and cell.shape != "-"):
                counter += 1
            if (cell.shape == "-"):
                counter_blank += 1
        if (shape+str(counter)) not in _states:
            _states[shape+str(counter)] = 0
        if (counter + counter_blank == 4):
            _states[shape+str(counter)] += 1
    
    # stop = timeit.default_timer()
    # print('Time: ', stop - start) 
    # print(_states)

def countStateValue(_state, _player):
    valid_colors = ["BLUE", "RED"]
    valid_shapes = ["X", "O"]
    weights = {
        "SHAPE1":5,
        "SHAPE2":10,
        "SHAPE3":30,
        "SHAPE4":100,
        "COLOR1":1,
        "COLOR2":7,
        "COLOR3":20,
        "COLOR4":100 }
    player_shape = _player.shape
    player_color = _player.color
    total = 0
    end = False
    
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
    end = (player_shape + "4" in key) or (player_color + "4" in key)
    if (end): print(key)

    print(_state, total)
    return (total, end)

#Your statements here
# start = timeit.default_timer()

# matrix = np.arange(42).reshape(6, 7)
# print(matrix)

def rollingWindow(a, window_size):
    shape = (a.shape[0] - window_size + 1, window_size) + a.shape[1:]
    strides = (a.strides[0],) + a.strides
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

def runSplitHV(a):
    result = []
    x = a.transpose()
    # for row in a:
    #     temp = rollingWindow(row, 4)
    #     for group in temp: result.append(group)

    

    # for row in x:
    #     temp = rollingWindow(row, 4)
    #     for group in temp: result.append(group)

    for i in range(len(a)):
        tempA = rollingWindow(a[i], 4)
        for groupA in tempA: result.append(groupA)

        tempX = rollingWindow(x[i], 4)
        for groupX in tempX: result.append(groupX)
    return result

def splitDiagonal(a):
    # print("Diagonal")
    result = []
    for i in range(-3, 4):
        diagonal = np.diagonal(a, offset=i)
        if (len(diagonal) >= 4):
            temp = rollingWindow(diagonal, 4)
            for group in temp: result.append(group)
    # print("Len diagonal: " + str(len(result)))
    return result

def runSplitDiagonal(a):
    flipped = np.fliplr(a)
    return (splitDiagonal(a) + splitDiagonal(flipped))

# runSplitHV(matrix)
# runSplitDiagonal(matrix)

# stop = timeit.default_timer()
# # print('Time: ', stop - start)  


    


