import pygame

class Tile:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
class Board:
    def __init__(self, row, col):
        self.board = []
        for r in range(row):
            for c in range(col):
                self.board.append(Tile(r, c))
        

def print_tiles(board):
    for tile in board.board:
        print( (tile.x, tile.y) )

board = Board(2, 2)
print_tiles(board)