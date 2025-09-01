#
from dataclasses import dataclass

@dataclass
class Pattern:
    name: str
    alive_cells: list[tuple[int, int]]