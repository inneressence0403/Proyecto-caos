#agrega una clase Pattern con funcionalidades __int__, __repr y __eq__ (útilpara debuging)
from dataclasses import dataclass

@dataclass
class Pattern:
    name: str
    alive_cells: list[tuple[int, int]]
