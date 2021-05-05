import numpy as np
from towersRules import *


def solveTower(nPieces, reportIncrement = 0):
    x = towersGameBoard(nPieces)
    curIncrement = [1]
    reportStatus(x, reportIncrement, curIncrement)
    recTowers(x, nPieces, 'A', 'C', 'B', reportIncrement, curIncrement)

def recTowers(gb, nPieces, fromPeg, toPeg, auxPeg, reportIncrement, curIncrement):
    if nPieces == 1:
        gb.movePiece(fromPeg, toPeg)
        reportStatus(gb, reportIncrement, curIncrement)
    else:
        recTowers(gb, nPieces - 1, fromPeg, auxPeg, toPeg, reportIncrement, curIncrement)
        
        gb.movePiece(fromPeg, toPeg)
        reportStatus(gb, reportIncrement, curIncrement)
        
        recTowers(gb, nPieces - 1, auxPeg, toPeg, fromPeg, reportIncrement, curIncrement)
    
def reportStatus(gb, reportIncrement, curIncrement):
    if reportIncrement == 0:
        return
    if curIncrement[0] == 1:
        print("\n" + gb.view())
        curIncrement[0] = reportIncrement
        return
    curIncrement[0] -= 1
    return

