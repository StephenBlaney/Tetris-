import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800 # Screen Width
s_height = 700 # Screen Height
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30 # Size of our Tetris blocks in the game

top_left_x = (s_width - play_width) // 2 #represents the top left area checking for collision
top_left_y = s_height - play_height


# SHAPE FORMATS
#This is what will represent our shapes in Tetris containing lists within lists the reason being is cause each sahpe has more then one rotation



#Var S represents the shape of an S in Tetris the second list is the second  rotation of S and so on
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

# Square
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    def __init__(self,x,y,shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shape.index(shape)] #the index of shape is our color
        self.rotation = 0 # This will be used later when we change our shapes from teh keyboard input

#GRID REPRESENTATION
def create_grid(locked_positions={}):
    grid = [[(0,0,0)for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions [(j,i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    return random.choice(shapes)


def draw_text_middle(text, size, color, surface):
    pass

def draw_grid(surface, grid):
    surface.fill(0,0,0)

    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 60) # Font set to comicssans
    label = font.render("Tetris", (255,255,255)) # Label color set to white

    surface.blit(label, (top_left_x + play_width/2 - label.get_width()/2), 30)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x +j*30, top_left_y+ i*30))

def clear_rows(grid, locked):


def draw_next_shape(shape, surface):


def draw_window(surface):
    pass

def main():
    pass

def main_menu():
    pass

main_menu()  # start game