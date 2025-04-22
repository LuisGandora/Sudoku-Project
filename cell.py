from pygame import *
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
    
    def set_cell_value(self, value):
        self.value = value
        self.draw()

    def set_sketched_value(self, value):
        cell_font = font.Font(None, 35)
        if(self.value > 0):
            cell_text = cell_font.render(f"{value}", 0, 'black')
        else:
            cell_text = cell_font.render(" ", 0, 'black')
        cell_surface = Surface((30,30))
        cell_surface.fill("thistle2")
        cell_surface.blit(cell_text, cell_text.get_rect(center=(15,15)))
        cell_rectangle = cell_surface.get_rect(center=(self.row, self.col))
        self.screen.blit(cell_surface,cell_rectangle)
        

    def draw(self,color="black"):
        cell_font = font.Font(None, 35)
        if(self.value > 0):
            cell_text = cell_font.render(f"{self.value}", 0, 'black')
        else:
            cell_text = cell_font.render(" ", 0, 'black')
        cell_surface = Surface((30,30))
        cell_surface.fill("thistle2")
        cell_surface.blit(cell_text, cell_text.get_rect(center=(15,15)))
        cell_rectangle = cell_surface.get_rect(center=(self.row, self.col))
        self.screen.blit(cell_surface,cell_rectangle)
    
    