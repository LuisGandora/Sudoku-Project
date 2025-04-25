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
        for i in range(0, 10):
            pygame.draw.line(self.screen, "black", (200+(i * 40), 100+0), (200+(i * 40), 100+360))
            pygame.draw.line(self.screen, "black", (200+0, 100+ i * 40), (200+360, 100+i * 40))
            if i == 0 or i == 3 or i == 6 or i == 9:
                line_width = 3
            else:
                line_width = 1
            pygame.draw.line(self.screen, "black", (200+(i * 40), 100+0), (200+(i * 40), 100+360), line_width)
            pygame.draw.line(self.screen, "black", (200+0, 100+ i * 40), (200+360, 100+i * 40), line_width)
        for j in range(len(self.board)):
            for k in range(len(self.board[0])):
                tempGameObject = Cell(self.board[j][k], (k * 40) + 220, (j * 40) + 120, self.screen)
                tempGameObject.draw()

        pygame.display.flip() #my attempt at improving

    def select(self, row, col):
        self.draw()
        x = 200 + ((row-200)//40) * 40
        y = 100 + ((col-100)//40) * 40
        print(self.board)
        if 200<=x<=520 and 100<=y<=420:
            pygame.draw.line(self.screen, "indianred", (x,y), (x,y+40), 5)
            pygame.draw.line(self.screen, "indianred", (x+40,y), (x+40,y+40), 5)
            pygame.draw.line(self.screen, "indianred", (x,y), (x+40,y), 5)
            pygame.draw.line(self.screen, "indianred", (x,y+40), (x+40,y+40), 5)
            pygame.display.update() #my attempt at improving
        


    #Not sure if its suppose to be bool return or none return
    def click(self, row, col):
        global x, y
        x = ((row-200)//40) 
        y = ((col-100)//40) 
        print("X" + f"{x}")
        print("Y" + f"{y}")
        print("Val" + f"{self.board[y][x]}" )
        if(x < len(self.board)):
            if(y < len(self.board[0])):
                return (row, col)
        return None

    def clear(self):
        #to do later
        print("Clear val")

    def sketch(self, value):
        pass
        #later

    def place_number(self, value):
        self.board[y][x] = value
        self.draw()

    def reset_to_original(self):
        #to do later
        print("reset")

    def is_full(self):
        for i in self.board:
            if(0 in i):
                return False
        return True
    
    def update_board(self):
        self.draw()


    def find_empty(self):
        #to do later
        print("empty board")


    def check_board(self):
        tempObj = SudokuGenerator(9, 0)
        tempObj.board = self.board
        for i in range(len(tempObj.board)):
            for j in range(len(tempObj.board[0])):
                if(not tempObj.is_valid(i, j, tempObj.board[i][j])):
                    return False
        return True


