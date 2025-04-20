import pygame, sys
from pygame.locals import *
from board import *
from sudoku_generator import *

#Initialize
pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
difficulty = 30 
clickedCords  = (0,0)
activeClick = False

#universal button
reset_board_button = pygame.Rect(0,0,0,0)   
reset_button = pygame.Rect(0,0,0,0)
quit_button = pygame.Rect(0,0,0,0)

#https://www.youtube.com/watch?v=U9H60qtw0Yg tutorial I followed
def start_screen():


    orig_image = pygame.image.load("cherry blueson.jpg")
    title_image = pygame.transform.scale(orig_image, (800,600))
    #initialize font
    start_title = pygame.font.Font(None, 200)
    button_font = pygame.font.Font(None, 80)
    #initialize background
    screen.blit(title_image, title_image.get_rect(topleft=(0, 0)))
    #Initialize Title
    title_surface = start_title.render("Sudoku", 0, 'white')
    title_rectangle = title_surface.get_rect(center =(WIDTH//2, HEIGHT//2 - 150))
    screen.blit(title_surface, title_rectangle)

    #initialize text for start and quit button
    Easy_text = button_font.render("Easy", 0, (255,255,255)) #30empty
    Medium_text = button_font.render("Medium", 0, (255,255,255))#40empty
    Hard_text = button_font.render("Hard", 0, (255,255,255))#50empty


    #All of this makes the surfaces for the start and quit button
    easy_surface = pygame.Surface((Easy_text.get_size()[0]+20, Easy_text.get_size()[1] + 20))
    easy_surface.fill('palevioletred1')
    easy_surface.blit(Easy_text, (10,10))
    Medium_surface = pygame.Surface((Medium_text.get_size()[0]+20, Medium_text.get_size()[1] + 20))
    Medium_surface.fill('palevioletred1')
    Medium_surface.blit(Medium_text, (10,10))
    Hard_surface = pygame.Surface((Hard_text.get_size()[0] + 20, Hard_text.get_size()[1]+20))
    Hard_surface.fill('palevioletred1')
    Hard_surface.blit(Hard_text, (10,10))
    Easy_rectangle = easy_surface.get_rect(center=(WIDTH //2, HEIGHT //2 +5))
    Medium_rectangle = Medium_surface.get_rect(center=(WIDTH //2, HEIGHT //2 +105)) ##RECOMMEND CHANGING TO WIDTH BASED INSTEAD like -109,105 0,105 and 109,105
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
                return 30
            if event.type ==pygame.MOUSEBUTTONDOWN: #Checks which button you press
                if Easy_rectangle.collidepoint(event.pos):
                    return 30
                    #change later
                elif Medium_rectangle.collidepoint(event.pos):
                    return 40
                elif Hard_rectangle.collidepoint(event.pos):
                    return 50
                    
        pygame.display.update()

def in_progress_menu():
    global reset_board_button, reset_button, quit_button
    #initialize font
    button_font = pygame.font.Font(None, 40)
    #initialize background
    screen.fill((255, 255, 255))

    #initialize text for reset, restart, exit buttons
    reset_text = button_font.render("Reset", 0, (255, 255, 255))  # 30empty
    restart_text = button_font.render("Restart", 0, (255, 255, 255))  # 40empty
    exit_text = button_font.render("Exit", 0, (255, 255, 255))  # 50empty

    #makes the surfaces for the reset, reset and exit buttons
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill((255, 176, 0))
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((255, 176, 0))
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((255, 176, 0))
    exit_surface.blit(exit_text, (10, 10))
    reset_board_button = reset_surface.get_rect(center=(WIDTH // 2 - 209, HEIGHT // 2 + 275))
    reset_button = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 275))
    quit_button = exit_surface.get_rect(center=(WIDTH // 2 + 190, HEIGHT // 2 + 275))

    #glues the surfaces to the rects to make sure they are visible on play
    screen.blit(reset_surface, reset_board_button)
    screen.blit(restart_surface, reset_button)
    screen.blit(exit_surface, quit_button)

def in_progress():
    global activeClick
    print("InProgress")
    start_board = Board(WIDTH, HEIGHT, screen, difficulty)
    start_board.board = generate_sudoku(9, start_board.difficulty)
    
    #Highly recommend switching to Universal reset_text 
    in_progress_menu()
    print(start_board.board)
    # Menu logic
    print("Ran")
    print(reset_board_button)
    while True:
        start_board.update_board() #later
        
        for event in pygame.event.get():  # essentially waits for user to input something
            if event.type == pygame.QUIT:  # If Escape, exit game
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Checks which button you press
                if reset_board_button.collidepoint(event.pos):
                    return  # change later
                elif reset_button.collidepoint(event.pos):
                    return
                elif quit_button.collidepoint(event.pos):
                    sys.exit()
                elif start_board.click(event.pos[0], event.pos[1]) != False:
                    in_progress_menu()
                    clickedCords = start_board.click(event.pos[0],event.pos[1])
                    start_board.select(clickedCords[0], clickedCords[1])
                    x = (clickedCords[0]//(start_board.width//9))
                    y =(clickedCords[1]//60)
                    print(x)
                    print(y)
                    print(start_board.board[x][y])
                    if(start_board.board[x][y] == 0):
                        activeClick = True
                        print("Activated")
                
                    
                else:
                    sys.exit()
            if event.type == pygame.KEYDOWN and activeClick:
                temp = event.key-48
                if(temp > 0 and temp < 10 and activeClick):
                    start_board.place_number(temp)
                    activeClick = False
                    start_board.draw()
                    print("Commited")
                    
        pygame.display.update()

def game_won():

    orig_image = pygame.image.load("cherry blueson.jpg")
    win_image = pygame.transform.scale(orig_image, (800,600))
    #initialize font
    win_text = pygame.font.Font(None, 115)
    button_font = pygame.font.Font(None, 80)
    #initialize background
    screen.blit(win_image, win_image.get_rect(topleft=(0, 0)))
    #initialize game_over   
    win_surface = win_text.render("Game Won <3", 0, (255,176,0))
    win_rectangle = win_surface.get_rect(center =(WIDTH//2, HEIGHT//2 - 150))
    screen.blit(win_surface, win_rectangle)

    #initialize text for restart button
    exit_text = button_font.render("Exit", 0, (255, 255, 255))  # 30empty

    #surface for the restart button
    win_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    win_surface.fill((255, 176, 0))
    win_surface.blit(exit_text, (10, 10))
    win_rectangle = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 5))

    #glues the surfaces to the rects to make sure they are visible on play
    screen.blit(win_surface, win_rectangle)

    #game_over logic
    while True:
        for event in pygame.event.get():  #waits for user to input something
            if event.type == pygame.QUIT:  #if escape, exit game
                return False  # exits main "While True" loop
            if event.type == pygame.MOUSEBUTTONDOWN:  #checks for exit button press
                if win_rectangle.collidepoint(event.pos):
                    return False #exits main "While True" loop

        pygame.display.update()

def game_over():

    orig_image = pygame.image.load("cherry blueson.jpg")
    end_image = pygame.transform.scale(orig_image, (800,600))
    #initialize font
    end_text = pygame.font.Font(None, 115)
    button_font = pygame.font.Font(None, 80)
    #initialize background
    screen.blit(end_image, end_image.get_rect(topleft=(0, 0)))
    #initialize game_over
    end_surface = end_text.render("Game Over </3", 0, (255,176,0))
    end_rectangle = end_surface.get_rect(center =(WIDTH//2, HEIGHT//2 - 150))
    screen.blit(end_surface, end_rectangle)

    #initialize text for restart button
    restart_text = button_font.render("Restart", 0, (255, 255, 255))  # 30empty

    #surface for the restart button
    end_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    end_surface.fill((255, 176, 0))
    end_surface.blit(restart_text, (10, 10))
    end_rectangle = end_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 5))

    #glues the surfaces to the rects to make sure they are visible on play
    screen.blit(end_surface, end_rectangle)

    #game_over logic
    while True:
        for event in pygame.event.get():  #waits for user to input something
            if event.type == pygame.QUIT:  #if escape, exit game
                return False  # exits main "While True" loop
            if event.type == pygame.MOUSEBUTTONDOWN:  #checks for restart button press
                if end_rectangle.collidepoint(event.pos):
                    return False #exits main "While True" loop

        pygame.display.update()

def main():
    while True:
        difficulty = start_screen()
        in_progress()
        game_won() #reposition later; just to check
        game_over() #reposition later; just to check


if __name__ == "__main__":
    main()
        