from solver import SudokuSolver
from HouseNum import HouseNum
from HouseType import HouseType

GIVENS = "5..62..37..489........5....93........2....6.57.......3.....9.........7..68.57...2"
solver = SudokuSolver()
solver.setup_board(GIVENS)

print(solver)

modified_cells = solver.hidden_subset(HouseType.COL, solver.get_board()[3][5])

for cell in modified_cells:
    print(cell)
