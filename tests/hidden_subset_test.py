import unittest

from solver import SudokuSolver
from SudokuCell import SudokuCell, EMPTY_CELL
from HouseNum import HouseNum
from HouseType import HouseType
from utils import HOUSE_COORDS_MAP, CELL_HOUSE_COORDS_MAP


# Taken from https://hodoku.sourceforge.net/en/show_example.php?file=h302&tech=Hidden+Triple.
GIVENS = "5..62..37..489........5....93........2....6.57.......3.....9.........7..68.57...2"


class TestSum(unittest.TestCase):

    # def test_naked_triple_first_overload(self):
    #     solver = SudokuSolver()
    #     solver.setup_board(GIVENS)
    #     solver.naked_subset()

    # def test_naked_triple_second_overload(self):
    #     solver = SudokuSolver()
    #     solver.setup_board(GIVENS)
    #     solver.naked_subset()

    def test_hidden_triple_third_overload(self):
        solver = SudokuSolver()
        solver.setup_board(GIVENS)
        modified_cells = solver.hidden_subset(HouseType.COL, solver.get_board()[3][5])
        self.assertEqual(len(modified_cells), 3)

        expected = {  # Coordinate (0-based indexing) to candidate mapping.
            (3, 5): {2, 5, 6},
            (5, 5): {2, 5, 6},
            (7, 5): {2, 6}
        }
        actual = {(cell.get_row(), cell.get_col()): cell.get_candidates() for cell in modified_cells}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
