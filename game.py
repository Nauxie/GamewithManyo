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



board = Board(9, 5)
print_tiles(board)

width = 800
height = 600
white = (255, 255, 255)

pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Focus')
clock = pygame.time.Clock()

ingame = True

while ingame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = False

    start_x, start_y = 100, 100
    for tile in board.board:
        pygame.draw.rect(gameDisplay, white, ((start_x + tile.x * 70, start_y + tile.y * 70, 70, 70)), 1 )
    pygame.display.update()
    clock.tick(30)
    