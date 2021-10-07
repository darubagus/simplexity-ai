import pickle
from typing import Tuple
from src.model import Piece, Board, State
from src.constant import ShapeConstant, GameConstant
from src.matrixProc import *

#INI BUAT TESTING
board = Board(6, 7)


def objective(_state : State, _player : int) -> int:
    """
    
    """
    # objective value dr shape1 : 1*X
    # objective value dr shape2 : 2*X
    # objective value dr shape3 : 3*X
    # objective value dr color1 : 0.5*X
    # objective value dr color2 : 1.5*X
    # objective value dr color3 : 2.5*X
    
    
    
def value(player : int) -> int:
    """
    player : player who is playing right now
    """
    return 0
def checkStreak(_state: State, playerID:int):
    pass

print(np.array(board))

