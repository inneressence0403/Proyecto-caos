import collections
import pygame
ALIVE = 1
DEAD = 0
class Grid:
    def __init__(self, width, height, cell_size): #inicializa el grid
        self.pattern = None
        #Creación de atributos
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.cell_size = cell_size
        self.cells = [[DEAD for _ in range(self.cols)] for _ in range(self.rows)]
    
    def draw(self, screen): #dibuja el grid
        for row in range(self.rows):
            for col in range(self.cols):
                color = (255, 255, 255) if self.cells[row][col] else (55, 55, 55)
                pygame.draw.rect(screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size -1, self.cell_size -1))
    def evolve(self):  # calcula la siguiente generación
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        new_cells = [[DEAD for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = 0
                for dr, dc in neighbors:
                    r = (row + dr) % self.rows
                    c = (col + dc) % self.cols
                    if self.cells[r][c] == ALIVE:
                        live_neighbors += 1
                if self.cells[row][col] == ALIVE:
                    if live_neighbors in (2, 3):
                        new_cells[row][col] = ALIVE
                    else:
                        new_cells[row][col] = DEAD
                else:
                    if live_neighbors == 3:
                        new_cells[row][col] = ALIVE
        self.cells = new_cells
        
   