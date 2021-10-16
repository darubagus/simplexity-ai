import random
from time import time
import copy

from src.constant import ShapeConstant
from src.model import State
from src.ai.objective import *
from src.utility import place

from typing import Tuple, List


class Minimax:
    def __init__(self):
        pass

    def find(self, state: State, n_player: int, thinking_time: float):
        self.thinking_time = time() + thinking_time

        result = self.minimax(state, 3, float("-inf"), float("inf"), True)
        best_movement = (result[1][0], result[1][1])
        print(result[0])
        print(best_movement)

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

    def minimax(self, state: State, depth: int, alpha: int, beta: int, maximizing: bool):
        boardCp = Board(state.board.row, state.board.col)
        boardCp.board = copy.deepcopy(state.board.board)
        playersCp = copy.deepcopy(state.players)
        stateCp = State(boardCp, playersCp, state.round)

        if (depth == 0):
            # print(objective(state))
            return (objective(state), (0, "-"))
        
        successorStates = self.generatePossibleMoves(stateCp)
        if (maximizing):
            maxScore = float("-inf")
            bestMove = ''
            for succState in successorStates:
                currScore = self.minimax(succState[0], depth-1, alpha, beta, False)[0]
                maxScore = max(maxScore, currScore)
                if (maxScore == currScore):
                    bestMove = (succState[1], succState[2])
                alpha = max(alpha, currScore)
                if (beta <= alpha):
                    break
            return (maxScore, bestMove)

        else:
            minScore = float("inf")
            bestMove = ""
            for succState in successorStates:
                currScore = self.minimax(succState[0], depth-1, alpha, beta, True)[0]
                minScore = min(minScore, currScore)
                if (minScore == currScore):
                    bestMove = (succState[1], succState[2])
                beta = min(beta, currScore)
                if (beta <= alpha):
                    break
            return (minScore, bestMove)
            

