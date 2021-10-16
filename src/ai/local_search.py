import random
import copy
from time import time
from src.ai.objective import objective

from src.constant import ShapeConstant
from src.model import State, Board
from src.utility import place

from typing import Tuple, List


class LocalSearch:
    def __init__(self):
        pass

    def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:
        self.thinking_time = time() + thinking_time

        result = self.sidewaysHillClimb(state)
        best_movement = (result[1][0], result[1][1])

        return best_movement

    def generatePossibleMoves(self, state: State):
        currentPlayer = (state.round - 1) % 2
        xValidity = state.players[currentPlayer].quota["X"] > 0
        oValidity = state.players[currentPlayer].quota["O"] > 0

        arrOfSuccStates = []
        if (xValidity):
            for i in range(state.board.col):
                boardCp = Board(state.board.row, state.board.col)
                boardCp.board = copy.deepcopy(state.board.board)
                playersCp = copy.deepcopy(state.players)
                stateCp = State(boardCp, playersCp, state.round + 1)

                placementSucc = place(stateCp, currentPlayer, "X", i)
                if (placementSucc != -1):
                    arrOfSuccStates.append((stateCp, i, ShapeConstant.CROSS))

        if (oValidity):
            for i in range(state.board.col):
                boardCp = Board(state.board.row, state.board.col)
                boardCp.board = copy.deepcopy(state.board.board)
                playersCp = copy.deepcopy(state.players)
                stateCp = State(boardCp, playersCp, state.round + 1)

                placementSucc = place(stateCp, currentPlayer, "O", i)
                if (placementSucc != -1):
                    arrOfSuccStates.append((stateCp, i, ShapeConstant.CIRCLE))
       
        return arrOfSuccStates      

    def sidewaysHillClimb(self, state: State):
        maxScore = objective(state)
        neighbor = (copy.deepcopy(state), random.randint(0, state.board.col), random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE]))
        backupNeighbor = (copy.deepcopy(state), random.randint(0, state.board.col), random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE]))
        nonCurrentHighest = float("-inf")
        bestMove = ()

        successors = self.generatePossibleMoves(state)

        for successor in successors:
            currentScore = objective(successor[0])
            if (maxScore <= currentScore):
                maxScore = currentScore
                neighbor = successor
            
            if (currentScore >= nonCurrentHighest):
                nonCurrentHighest = currentScore
                backupNeighbor = successor

        if (nonCurrentHighest == maxScore):
            return (maxScore, (neighbor[1], neighbor[2]))
        else:
            return (nonCurrentHighest, (backupNeighbor[1], backupNeighbor[2]))


            
            
        

        