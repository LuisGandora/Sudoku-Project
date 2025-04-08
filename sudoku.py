import pygame, sys
from pygame.locals import *
from board import *

#Initialize
pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#https://www.youtube.com/watch?v=U9H60qtw0Yg tutorial I followed
def start_screen():
    


    #initialize font
    start_title = pygame.font.Font(None, 100) 
    button_font = pygame.font.Font(None, 100)
    #initialize background
    screen.fill((255,255,255))
    #Initialize Title
    title_surface = start_title.render("Sudoku", 0, (255,176,0))
    title_rectangle = title_surface.get_rect(center =(WIDTH//2, HEIGHT//2 - 150))
    screen.blit(title_surface, title_rectangle)

    #initialize text for start and quit button
    start_text = button_font.render("Start", 0, (255,255,255))
    end_text = button_font.render("Quit", 0, (255,255,255))

    #All of this makes the surfaces for the start and quit button
    start_surface = pygame.Surface((start_text.get_size()[0]+20, start_text.get_size()[1] + 20))
    start_surface.fill((255,176,0))
    start_surface.blit(start_text, (10,10))
    quit_surface = pygame.Surface((end_text.get_size()[0] + 20, end_text.get_size()[1]+20))
    quit_surface.fill((255,176,0))
    quit_surface.blit(end_text, (10,10))
    start_rectangle = start_surface.get_rect(center=(WIDTH //2, HEIGHT //2 +50))
    quit_rectangle = quit_surface.get_rect(center=(WIDTH //2, HEIGHT //2 +150))


    #Essentially glues the surfaces to the rects to make sure they are visible on play
    screen.blit(start_surface, start_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    #Menu logic
    while True:
        for event in pygame.event.get(): #essentially waits for user to input something
            if event.type == pygame.QUIT: #If Escape, exit game
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN: #Checks which button you press
                if start_rectangle.collidepoint(event.pos):
                    return #change later
                elif quit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()

def main():

    start_screen()
    print("Main run")   

if __name__ == "__main__":
    main()