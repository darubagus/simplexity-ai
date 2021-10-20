import numpy as np
import timeit

#Your statements here
start = timeit.default_timer()

matrix = np.arange(42).reshape(6, 7)
print(matrix)

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

runSplitHV(matrix)
runSplitDiagonal(matrix)

stop = timeit.default_timer()
# # print('Time: ', stop - start)  


    

