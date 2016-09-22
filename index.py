"""Flask test."""
from flask import Flask, url_for, json, request, Response
import testForWinner
import numpy as numpy


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

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def api_root():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data
    elif request.headers['Content-Type'] == 'application/json':
        # return "JSON Message: " + json.dumps(request.json)
        json_data = request.json['message']
        return json_data[2]
    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run()
