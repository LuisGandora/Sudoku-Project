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
        self.board = None #passed in value

    def draw(self):
        for i in range(0, 10):
            if i == 0 or i == 3 or i == 6 or i == 9:
                line_width = 3
            else:
                line_width = 1
            pygame.draw.line(self.screen, "black", (200+(i * 40), 100+0), (200+(i * 40), 100+360), line_width)
            pygame.draw.line(self.screen, "black", (200+0, 100+ i * 40), (200+360, 100+i * 40), line_width)
        for j in range(len(self.board[0])):
            for k in range(len(self.board)):
                tempGameObject = Cell(self.board[j][k], (k * 40) + 220, (j * 40) + 120, self.screen)
                tempGameObject.draw()
        pygame.display.flip() #my attempt at improving

    def select(self, row, col):
        self.draw()
        x = 200 + ((row-200)//40) * 40
        y = 100 + ((col-100)//40) * 40
        if 200<=x<=520 and 100<=y<=420:
            pygame.draw.line(self.screen, "red", (x,y), (x,y+40), 5)
            pygame.draw.line(self.screen, "red", (x+40,y), (x+40,y+40), 5)
            pygame.draw.line(self.screen, "red", (x,y), (x+40,y), 5)
            pygame.draw.line(self.screen, "red", (x,y+40), (x+40,y+40), 5)
            pygame.display.update() #my attempt at improving


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


