import pygame, sys
from pygame.locals import *
from board import *

#Initialize
pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
difficulty = 30 

#https://www.youtube.com/watch?v=U9H60qtw0Yg tutorial I followed
def start_screen():
    


    #initialize font
    start_title = pygame.font.Font(None, 200)
    button_font = pygame.font.Font(None, 80)
    #initialize background
    screen.fill((255,255,255))
    #Initialize Title
    title_surface = start_title.render("Sudoku", 0, (255,176,0))
    title_rectangle = title_surface.get_rect(center =(WIDTH//2, HEIGHT//2 - 150))
    screen.blit(title_surface, title_rectangle)

    #initialize text for start and quit button
    Easy_text = button_font.render("Easy", 0, (255,255,255)) #30empty
    Medium_text = button_font.render("Medium", 0, (255,255,255))#40empty
    Hard_text = button_font.render("Hard", 0, (255,255,255))#50empty


    #All of this makes the surfaces for the start and quit button
    easy_surface = pygame.Surface((Easy_text.get_size()[0]+20, Easy_text.get_size()[1] + 20))
    easy_surface.fill((255,176,0))
    easy_surface.blit(Easy_text, (10,10))
    Medium_surface = pygame.Surface((Medium_text.get_size()[0]+20, Medium_text.get_size()[1] + 20))
    Medium_surface.fill((255,176,0))
    Medium_surface.blit(Medium_text, (10,10))
    Hard_surface = pygame.Surface((Hard_text.get_size()[0] + 20, Hard_text.get_size()[1]+20))
    Hard_surface.fill((255,176,0))
    Hard_surface.blit(Hard_text, (10,10))
    Easy_rectangle = easy_surface.get_rect(center=(WIDTH //2, HEIGHT //2 +5))
    Medium_rectangle = Medium_surface.get_rect(center=(WIDTH //2, HEIGHT //2 +105))
    Hard_rectangle = Hard_surface.get_rect(center=(WIDTH //2, HEIGHT //2 +205))


    #Essentially glues the surfaces to the rects to make sure they are visible on play
    screen.blit(easy_surface, Easy_rectangle)
    screen.blit(Medium_surface, Medium_rectangle)
    screen.blit(Hard_surface, Hard_rectangle)
    

    #Menu logic
    while True:
        for event in pygame.event.get(): #essentially waits for user to input something
            if event.type == pygame.QUIT: #If Escape, exit game
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN: #Checks which button you press
                if Easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                    return #change later
                elif Medium_rectangle.collidepoint(event.pos):
                    difficulty = 40
                    return
                elif Hard_rectangle.collidepoint(event.pos):
                    difficulty = 50
                    
        pygame.display.update()

def main():

    start_screen()
    start_board = Board(WIDTH, HEIGHT, screen, difficulty)
    start_board.draw() #later

if __name__ == "__main__":
    main()