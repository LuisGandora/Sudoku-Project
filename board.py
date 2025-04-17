from sudoku_generator import *
from cell import *
import pygame, sys
from pygame.locals import *

class Board:
    def __init__(self, width, height, screen, difficulty): #I believe should call sudoku generator here
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = None #passed in value
        
    def draw(self):

        for i in range(1,9):
            pygame.draw.line(self.screen, "black", (i * (self.width//9), 0),(i * (self.width//9),550), 1)
        for j in range(1,10):
            pygame.draw.line(self.screen, "black", (0,j * 60),(800,j * 60), 1)
        pygame.display.flip()

    def select(self, row, col):
        #to do later
        print("selected")

    def click(self, row, col):
        #to do later
        print("Click selected")

    def clear(self):
        #to do later
        print("Clear val")
        
    def place_number(self, value):
        #to do later
        print("placed and enter pressed")

    def reset_to_original(self):
        #to do later
        print("reset")

    def is_full(self):
        #to do later
        return True
    
    def update_board():
        #to do layer
        print("Updated board")

    def find_empty(self):
        #to do later
        print("empty board")

    def check_board(self):
        #to do later
        print("Board tuah")


