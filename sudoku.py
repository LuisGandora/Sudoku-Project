import pygame, sys
from pygame.locals import *
from board import *
from sudoku_generator import *

# Initialize
pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
difficulty = 30
clickedCords = (0, 0)
activeClick = False
currentCell = None

# universal button
reset_board_button = pygame.Rect(0, 0, 0, 0)
restart_button = pygame.Rect(0, 0, 0, 0)
quit_button = pygame.Rect(0, 0, 0, 0)

#universal button
reset_board_button = pygame.Rect(0,0,0,0)
reset_button = pygame.Rect(0,0,0,0)
quit_button = pygame.Rect(0,0,0,0)
def get_outline(image,color=(0,0,0)):
    """Returns an outlined image of the same size.  the image argument must
    either be a convert surface with a set colorkey, or a convert_alpha
    surface. color is the color which the outline will be drawn."""
    rect = image.get_rect()
    mask = pygame.mask.from_surface(image)
    outline = mask.outline()
    outline_image = pygame.Surface(rect.size).convert_alpha()
    outline_image.fill((0,0,0,0))
    for point in outline:
        outline_image.set_at(point,color)
    return outline_image


# https://www.youtube.com/watch?v=U9H60qtw0Yg tutorial I followed
def start_screen():
    orig_image = pygame.image.load("cherry blueson.jpg")
    title_image = pygame.transform.scale(orig_image, (800,600))
    miku1 = pygame.image.load("sakura miku 1.png")
    miku1_img = pygame.transform.scale(miku1, (250,350))
    miku1_outline = get_outline(miku1_img, color = (255, 255, 255))
    #initialize font
    title_image = pygame.transform.scale(orig_image, (800, 600))
    # initialize font
    start_title = pygame.font.Font(None, 200)
    button_font = pygame.font.Font(None, 80)
    # initialize background
    screen.blit(title_image, title_image.get_rect(topleft=(0, 0)))
    # Initialize Title
    screen.blit(miku1_outline, (500,250))
    screen.blit(miku1_img, (500,250))
    #Initialize Title
    title_surface = start_title.render("Sudoku", 0, 'white')
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # initialize text for start and quit button
    Easy_text = button_font.render("Easy", 0, (255, 255, 255))  # 30empty
    Medium_text = button_font.render("Medium", 0, (255, 255, 255))  # 40empty
    Hard_text = button_font.render("Hard", 0, (255, 255, 255))  # 50empty

    # All of this makes the surfaces for the start and quit button
    easy_surface = pygame.Surface((Easy_text.get_size()[0] + 20, Easy_text.get_size()[1] + 20))
    easy_surface.fill('palevioletred1')
    easy_surface.blit(Easy_text, (10, 10))
    Medium_surface = pygame.Surface((Medium_text.get_size()[0] + 20, Medium_text.get_size()[1] + 20))
    Medium_surface.fill('palevioletred1')
    Medium_surface.blit(Medium_text, (10, 10))
    Hard_surface = pygame.Surface((Hard_text.get_size()[0] + 20, Hard_text.get_size()[1] + 20))
    Hard_surface.fill('palevioletred1')
    Hard_surface.blit(Hard_text, (10, 10))
    Easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 5))
    Medium_rectangle = Medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 105))  ##RECOMMEND CHANGING TO WIDTH BASED INSTEAD like -109,105 0,105 and 109,105
    Hard_rectangle = Hard_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 205))

    # Essentially glues the surfaces to the rects to make sure they are visible on play
    screen.blit(easy_surface, Easy_rectangle)
    screen.blit(Medium_surface, Medium_rectangle)
    screen.blit(Hard_surface, Hard_rectangle)

    # Menu logic
    while True:
        for event in pygame.event.get():  # essentially waits for user to input something
            if event.type == pygame.QUIT:  # If Escape, exit game
                sys.exit()
                return 30
            if event.type == pygame.MOUSEBUTTONDOWN:  # Checks which button you press
                if Easy_rectangle.collidepoint(event.pos):
                    return 30
                    # change later
                elif Medium_rectangle.collidepoint(event.pos):
                    return 40
                elif Hard_rectangle.collidepoint(event.pos):
                    return 50

        pygame.display.update()


def in_progress_menu():
    global reset_board_button, restart_button, quit_button
    # initialize font
    button_font = pygame.font.Font(None, 40)
    # initialize background
    screen.fill("thistle2")

    # initialize text for reset, restart, exit buttons
    miku2 = pygame.image.load("sakura miku 7.png")
    miku2_img = pygame.transform.scale(miku2, (310, 200))
    miku2_outline = get_outline(miku2_img, color=(255, 255, 255))
    screen.blit(miku2_outline, (-5, 425))
    screen.blit(miku2_img, (-5, 425))
    #initialize text for reset, restart, exit buttons
    reset_text = button_font.render("Reset", 0, (255, 255, 255))  # 30empty
    restart_text = button_font.render("Restart", 0, (255, 255, 255))  # 40empty
    exit_text = button_font.render("Exit", 0, (255, 255, 255))  # 50empty

    # makes the surfaces for the reset, restart and exit buttons
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill("palevioletred1")
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill("palevioletred1")
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill("palevioletred1")
    exit_surface.blit(exit_text, (10, 10))
    reset_board_button = reset_surface.get_rect(center=(WIDTH // 2 - 209, HEIGHT // 2 + 225))
    restart_button = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 225))
    quit_button = exit_surface.get_rect(center=(WIDTH // 2 + 190, HEIGHT // 2 + 225))

    # glues the surfaces to the rects to make sure they are visible on play
    screen.blit(reset_surface, reset_board_button)
    screen.blit(restart_surface, restart_button)
    screen.blit(exit_surface, quit_button)


def in_progress(difficulty):
    global activeClick, currentCell
    print("InProgress")
    start_board = Board(WIDTH, HEIGHT, screen, difficulty)
    start_board.board = generate_sudoku(9, start_board.difficulty)
    original_board = []
    for row in start_board.board:
        original_board.append(row[:])

    # Highly recommend switching to Universal reset_text
    in_progress_menu()
    print(start_board.board)
    # Menu logic
    print("Ran")
    print(reset_board_button)
    while True:
        start_board.update_board()  # later
        if (currentCell != None):
            currentCell.draw()
        for event in pygame.event.get():  # essentially waits for user to input something
            if event.type == pygame.QUIT:  # If Escape, exit game
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Checks which button you press
                if reset_board_button.collidepoint(event.pos):
                    start_board.board = [row[:] for row in original_board]
                    currentCell = None
                    activeClick = False
                    start_board.draw()
                elif restart_button.collidepoint(event.pos):
                    return "restart"
                elif quit_button.collidepoint(event.pos):
                    sys.exit()
                elif start_board.click(event.pos[0], event.pos[1]) != False:
                    in_progress_menu()
                    clickedCords = start_board.click(event.pos[0], event.pos[1])
                    activeClick = False
                    x = ((clickedCords[0] - 200) // 40)
                    y = ((clickedCords[1] - 100) // 40)
                    start_board.select(clickedCords[0], clickedCords[1]) #Took this out of the if statement below; now you can click anywhere :)
                    if (original_board[y][x] == 0):
                        activeClick = True
                        print("Activated")
                # elif start_board.click(event.pos[0], event.pos[1]) != False:    THIS old code lets you select any cell but also breaks it and lets u edit them...
                #     in_progress_menu()
                #     clickedCords = start_board.click(event.pos[0],event.pos[1])
                #     start_board.select(clickedCords[0], clickedCords[1])
                #     x = ((clickedCords[0]-200)//40)
                #     y = ((clickedCords[1]-100)//40)
                #     if(start_board[y][x] == 0):
                #         activeClick = True
                #         print("Activated")


                else:
                    sys.exit()
            if event.type == pygame.KEYDOWN and activeClick:
                temp = event.key - 48
                # adding a cell board
                if (temp > 0 and temp < 10 and activeClick):
                    currentCell = Cell(temp, 200 + ((clickedCords[0]-200)//40) * 40+20, 100 + ((clickedCords[1]-100)//40) * 40+20, start_board.screen)
                    currentCell.draw()
                    start_board.draw()
                    print("Commited")
                if event.key == pygame.K_RETURN and activeClick:
                    if(currentCell != None):
                        start_board.place_number(currentCell.value)
                    currentCell = None
                    activeClick = False
                    start_board.draw()
                    if start_board.is_full() is True and start_board.check_board() is False:
                        return "Game Over"

                    if start_board.is_full() is True and start_board.check_board() is True:
                        return "Game Won"

        pygame.display.update()


def game_won():
    orig_image = pygame.image.load("bike.webp")
    win_image = pygame.transform.scale(orig_image, (800, 600))
    miku4 = pygame.image.load("sakura miku 4.png")
    miku4_img = pygame.transform.scale(miku4, (300, 400))
    miku4_outline = get_outline(miku4_img, color=(255, 255, 255))
    # initialize font
    win_text = pygame.font.Font(None, 115)
    button_font = pygame.font.Font(None, 80)
    # initialize background
    screen.blit(win_image, win_image.get_rect(topleft=(0, 0)))
    screen.blit(miku4_outline, (250, 200))
    screen.blit(miku4_img, (250, 200))
    # initialize game_won
    win_surface = win_text.render("Game Won <3", 0, "white")
    win_rectangle = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(win_surface, win_rectangle)

    # initialize text for exit button
    exit_text = button_font.render("Exit", 0, (255, 255, 255))  # 30empty

    # surface for the win
    win_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    win_surface.fill("palevioletred1")
    win_surface.blit(exit_text, (10, 10))
    win_rectangle = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 170))

    # glues the surfaces to the rects to make sure they are visible on play
    screen.blit(win_surface, win_rectangle)

    # game_won logic
    while True:
        for event in pygame.event.get():  # waits for user to input something
            if event.type == pygame.QUIT:  # if escape, exit game
                sys.exit() # exits main "While True" loop
            if event.type == pygame.MOUSEBUTTONDOWN:  # checks for exit button press
                if win_rectangle.collidepoint(event.pos):
                    sys.exit()
                    #return False  # exits main "While True" loop

        pygame.display.update()


def game_over():

    orig_image = pygame.image.load("treedark.jpg")
    end_image = pygame.transform.scale(orig_image, (800,600))
    #initialize font
    end_text = pygame.font.Font(None, 115)
    button_font = pygame.font.Font(None, 80)
    # initialize background
    screen.blit(end_image, end_image.get_rect(topleft=(0, 0)))
    # initialize game_over
    end_surface = end_text.render("Game Over </3", 0, "white")
    end_rectangle = end_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(end_surface, end_rectangle)

    # initialize text for restart button
    restart_text = button_font.render("Restart", 0, (255, 255, 255))  # 30empty

    # surface for the restart button
    end_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    end_surface.fill("palevioletred1")
    end_surface.blit(restart_text, (10, 10))
    end_rectangle = end_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 170 ))

    # glues the surfaces to the rects to make sure they are visible on play
    screen.blit(end_surface, end_rectangle)

    # game_over logic
    while True:
        for event in pygame.event.get():  # waits for user to input something
            if event.type == pygame.QUIT:  # if escape, exit game
                return False  # exits main "While True" loop
            if event.type == pygame.MOUSEBUTTONDOWN:  # checks for restart button press
                if end_rectangle.collidepoint(event.pos):
                    return False  # exits main "While True" loop
        pygame.display.update()


def main():
    while True:
        difficulty = start_screen()
        game_state = in_progress(difficulty)
        if game_state == "restart":
            continue
        elif game_state == "Game Won":
            game_won()
        elif game_state == "Game Over":
            game_over()


if __name__ == "__main__":
    main()
