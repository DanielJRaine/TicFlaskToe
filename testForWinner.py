import numpy as numpy

# player_x = 1
# player_o = -1

def checkForWin(player, cells):
    k = 3
    m = k
    n = k
    board = numpy.reshape(cells, (m, n), 'C')
    horizontalWin = k*player in board.sum(axis = 1)
    verticalWin = k*player in board.sum(axis = 0)
    mainDiagonalWin = k*player == board.trace()
    minorDiagonalWin = k*player == numpy.fliplr(board).trace()
    if horizontalWin or verticalWin or mainDiagonalWin or minorDiagonalWin:
        return True
    else:
        return False
