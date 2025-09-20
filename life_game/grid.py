import collections
ALIVE = "♥"
DEAD = "."
#agrega una clase LifeGrid con funcionalidades __init__, evolve, as_string y __str
class LifeGrid:
    def __init__(self, pattern): #inicializa el grid con un patron dado
        self.pattern = pattern
    def evolve(self): #calcula la siguiente generacion
        neighbors = {
            (-1,-1),(-1,0),(-1,1),
            (0,-1),       (0,1),
            (1,-1),(1,0),(1,1)
            }
        num_neighbors = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for dr, dc in neighbors:
                num_neighbors[row + dr, col + dc] += 1 
                 
        #condiciones de nacimiento y supervivencia
        stay_alive = {cell for cell in self.pattern.alive_cells if num_neighbors[cell] in (2, 3)}
        come_alive = {cell for cell, count in num_neighbors.items() if count == 3 and cell not in self.pattern.alive_cells}
        self.pattern.alive_cells = stay_alive | come_alive
        
    def as_string(self,bbox): #devuelve una representacion en string del grid
        start_col, start_row, end_col, end_row = bbox
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        for row in range(start_row, end_row):
            display_row = [
            ALIVE if (row, col) in self.pattern.alive_cells else DEAD
            for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        return "\n".join(display)
    def __str__(self): #devuelve una representacion en string del grid
       return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )
      