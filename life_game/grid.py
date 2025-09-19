import collections
class life_grid:
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
                num_neighbors[row + dr, col + dc] +=1 
                 
        #condiciones de nacimiento y supervivencia
        stay_alive = {cell for cell in self.pattern.alive_cells if num_neighbors[cell] in (2, 3)}
        come_alive = {cell for cell, count in num_neighbors.items() if count == 3 and cell not in self.pattern.alive_cells}
        self.pattern.alive_cells = stay_alive | come_alive
        pass
    def as_string(self,bbox): #devuelve una representacion en string del grid
        pass
    def __str__(self): #devuelve una representacion en string del grid
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )
    pass     