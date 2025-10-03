import pygame, sys
import time
from grid import Grid   

pygame.init()


#Creación de colores
BLACK = (0, 0, 0)
GREY = (33, 33, 33)
WHITE = (255, 255, 255)

#Definiciones 
WIDTH, HEIGHT = 1280, 720 #Dimensiones de la ventana
CELL_SIZE = 20 #Para el tamño de cada celda
FPS = 60
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life") #Se sefine una función para darle un título a la ventana

clock = pygame.time.Clock() #Controlar la velocidad de cuadros de la simulación. Qué tan rápido se ejecutará.

grid = Grid(WIDTH, HEIGHT, CELL_SIZE)

grid.cells[10][10] = 1
grid.cells[10][11] = 1  
grid.cells[10][12] = 1


def main():
    last_update = time.time()
    GENERATION_TIME = 0.5  # segundos por generación
    running = True
    while running:
        for event in pygame.event.get(): #Se obtienen los eventos que pygame ha reconocido 
            if event.type == pygame.QUIT: #Si el evento es de tipo QUIT se cierra la ventana. Salimos del bucle while.
                running = False
                
        now = time.time()
        if now - last_update > GENERATION_TIME:
            grid.evolve()
            last_update = now
            
        screen.fill(GREY) #Rellenar la pantalla con color gris
        grid.draw(screen) 
        pygame.display.update() #Actualizar la pantalla
        clock.tick(FPS)  #El bucle while se ejecutará a la velocidad definida, 60 veces por segundo como máximo.
    
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()

