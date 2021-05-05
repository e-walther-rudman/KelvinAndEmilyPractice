import numpy as np

class towersRod:
    def __init__(self, nPieces = 0):
        self.pieces = []
        self.pieces[:] = range(nPieces, 0 , -1)

    def peek(self):
        return self.pieces[len(self.pieces)-1]
    def pop(self):
        return self.pieces.pop()
    def push(self, x):
        self.pieces.append(x)
    def empty(self):
        return len(self.pieces)==0
    


class towersGameBoard:
    def __init__(self, nPieces):
        self.gameBoard = {'A': towersRod(nPieces),
                          'B': towersRod(),
                          'C': towersRod()}


    def view(self):
        gb = self.gameBoard
        returnString = "=================================\n"
        height = 0
        for key in gb:
            if height < len(gb[key].pieces):
                height = len(gb[key].pieces)

        while height > 0:
            returnString += "|\t"
            for key in gb:
                if height <= len(gb[key].pieces):
                    returnString = returnString + str(gb[key].pieces[height-1])
                returnString = returnString + "\t"
            returnString = returnString + "|\n"
            height -= 1
        returnString += "|\t"
        for key in gb:
            returnString = returnString + key + "\t"
        returnString += "|\n================================="
        return(returnString)

    def movePiece(self, fromRod, toRod):
        gb = self.gameBoard
        if gb[fromRod].empty():
            print("There is no piece on Rod " + fromRod)
            return False
        
        if gb[toRod].empty() or gb[fromRod].peek() < gb[toRod].peek():
            piece = gb[fromRod].pop()
            gb[toRod].push(piece)
            print("Piece (" + str(piece) + ") moved from Rod "
                  + fromRod + " to Rod " + toRod)
            return True
        else:
            print( "Illegal move: piece (" + str(gb[fromRod].peek())
                  + ") from rod " + fromRod + " is larger than ("
                  + str(gb[toRod].peek()) + "), the top piece of Rod " + toRod)
            return False
            



