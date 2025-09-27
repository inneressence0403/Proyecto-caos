import pygame, sys
import time
from grid import Grid   

pygame.init()  

BLACK = (0, 0, 0)
GREY = (33, 33, 33)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 1280, 720
CELL_SIZE = 20
FPS = 60
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()

grid = Grid(WIDTH, HEIGHT, CELL_SIZE)

grid.cells[10][10] = 1
grid.cells[10][11] = 1  
grid.cells[10][12] = 1


def main():
    last_update = time.time()
    GENERATION_TIME = 0.5  # segundos por generación
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        now = time.time()
        if now - last_update > GENERATION_TIME:
            grid.evolve()
            last_update = now
            
        screen.fill(GREY) 
        grid.draw(screen) 
        pygame.display.update()   
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()

