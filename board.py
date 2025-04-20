from sudoku_generator import *
from cell import *
import pygame, sys
from pygame.locals import *
x = 0 
y = 0
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
        for k in range(len(self.board[0])):
            for n in range(len(self.board)):
                tempGameObject = Cell(self.board[k][n],(n * self.width//9)+45, (k *60)+30, self.screen)
                tempGameObject.draw()
        pygame.display.flip()

    def select(self, row, col):
        self.draw()
        x = (row//(self.width//9)) * (self.width//9)
        y =(col//60) * 60
        pygame.draw.line(self.screen, "red", (x,y), (x,y+60), 5)
        pygame.draw.line(self.screen, "red", (x+90,y), (x+90,y+60), 5)
        pygame.draw.line(self.screen, "red", (x,y), (x+90,y), 5)
        pygame.draw.line(self.screen, "red", (x,y+60), (x+90,y+60), 5)
        pygame.display.update() #work on later


    #Not sure if its suppose to be bool return or none return
    def click(self, row, col):
        global x,y  
        x = (row//(self.width//9))
        y =(col//60)
        if(x < len(self.board)):
            if(y < len(self.board[0])):
                return (row, col)
        return None

    def clear(self):
        #to do later
        print("Clear val")
        
    def place_number(self, value):
        self.board[y][x] = value
        self.draw()
        print("placed and enter pressed")

    def reset_to_original(self):
        #to do later
        print("reset")

    def is_full(self):
        #to do later
        return True
    
    def update_board(self):
        self.draw()


    def find_empty(self):
        #to do later
        print("empty board")

    def check_board(self):
        #to do later
        print("Board tuah")


