from pygame import *
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
    
    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self,value):
        #to do later
        print("Temp")

    def draw(self):
        cell_font = font.Font(None, 40)
        cell_text = cell_font.render(f"{self.value}", 0, 'red')
        cell_surface = Surface((cell_text.get_size()[0]+30, cell_text.get_size()[1]+30))
        cell_surface.blit(cell_text, (10,10))
        cell_rectangle = cell_surface.get_rect(center=(self.row, self.col))
        self.screen.blit(cell_surface,cell_rectangle)
        display.flip()

    
    