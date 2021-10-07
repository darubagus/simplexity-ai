import numpy as np
import random

def ver(matrix,i,j):
    if(i>=4):
        i=4
    return[matrix[i][j],matrix[i+1][j],matrix[i+2][j],matrix[i+3][j]]

def dia(matrix,i,j):
    if(i>=4):
        i=4
    if(j>=3):
        j=3
    return[matrix[i][j],matrix[i+1][j+1],matrix[i+2][j+2],matrix[i+3][j+3]]

def hor(matrix,i,j):
    if(j>=3):
        j=3
    return[matrix[i][j],matrix[i][j+1],matrix[i][j+2],matrix[i][j+3]]
    
board_sample = [[j for j in range(7)] for i in range(6)]

WINDOW_1 = 1
WINDOW_2 = 4

random_matrix = np.random.randint(10, size=(6, 7))
print(random_matrix)
#random_matrix.reshape(random_matrix,(1, 4))
#a = np.reshape(random_matrix,(1,4))

#print(a)
print(hor(random_matrix,0,4))
