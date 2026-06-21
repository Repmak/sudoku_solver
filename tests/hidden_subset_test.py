import unittest

from solver import SudokuSolver
from SudokuCell import EMPTY_CELL
from HouseNum import HouseNum
from HouseType import HouseType


# Taken from https://hodoku.sourceforge.net/en/show_example.php?file=h302&tech=Hidden+Triple.
GIVENS = "5..62..37..489........5....93........2....6.57.......3.....9.........7..68.57...2"


class TestSum(unittest.TestCase):

    def test_hidden_triple_dispatch_1(self):
        solver = SudokuSolver()
        solver.setup_board(GIVENS)

        # Coordinate to candidate mapping. Coordinates use 0-based indexing and are formatted as (row, col).
        expected_candidates = {
            (3, 5): {2, 5, 6},
            (5, 5): {2, 5, 6},
            (7, 5): {2, 6}
        }
        expected_values = {
            (3, 5): EMPTY_CELL,
            (5, 5): EMPTY_CELL,
            (7, 5): EMPTY_CELL
        }

        """
        ^ indicates the column being targeted.
        5.. 62. .37
        ..4 89. ...
        ... .5. ...
        93. ... ...
        .2. ... 6.5
        7.. ... ..3
        ... ..9 ...
        ... ... 7..
        68. 57. ..2
              ^
        """
        modified_cells = solver.hidden_subset(HouseNum.SIX, HouseType.COL)
        actual_candidates = {(cell.get_row(), cell.get_col()): cell.get_candidates() for cell in modified_cells}
        actual_values = {(cell.get_row(), cell.get_col()): cell.get_value() for cell in modified_cells}

        self.assertEqual(actual_candidates, expected_candidates)
        self.assertEqual(actual_values, expected_values)

    def test_hidden_triple_dispatch_2(self):
        solver = SudokuSolver()
        solver.setup_board(GIVENS)

        # Coordinate to candidate mapping. Coordinates use 0-based indexing and are formatted as (row, col).
        expected_candidates = {
            (3, 5): {2, 5, 6},
            (5, 5): {2, 5, 6},
            (7, 5): {2, 6}
        }
        expected_values = {
            (3, 5): EMPTY_CELL,
            (5, 5): EMPTY_CELL,
            (7, 5): EMPTY_CELL
        }

        """
        # indicates the cell being passed in.
        5.. 62. .37
        ..4 89. ...
        ... .5. ...
        93. ..# ...
        .2. ... 6.5
        7.. ... ..3
        ... ..9 ...
        ... ... 7..
        68. 57. ..2
        """
        modified_cells = solver.hidden_subset(solver.get_cell(3, 5))
        actual_candidates = {(cell.get_row(), cell.get_col()): cell.get_candidates() for cell in modified_cells}
        actual_values = {(cell.get_row(), cell.get_col()): cell.get_value() for cell in modified_cells}

        self.assertEqual(actual_candidates, expected_candidates)
        self.assertEqual(actual_values, expected_values)

    def test_hidden_triple_dispatch_3(self):
        solver = SudokuSolver()
        solver.setup_board(GIVENS)

        # Coordinate to candidate mapping. Coordinates use 0-based indexing and are formatted as (row, col).
        expected_candidates = {
            (3, 5): {2, 5, 6},
            (5, 5): {2, 5, 6},
            (7, 5): {2, 6}
        }
        expected_values = {
            (3, 5): EMPTY_CELL,
            (5, 5): EMPTY_CELL,
            (7, 5): EMPTY_CELL
        }

        """
        # indicates the cell being targeted.
        ^ indicates the column being targeted.
        5.. 62. .37
        ..4 89. ...
        ... .5. ...
        93. ..# ...
        .2. ... 6.5
        7.. ... ..3
        ... ..9 ...
        ... ... 7..
        68. 57. ..2
              ^
        """
        modified_cells = solver.hidden_subset(HouseType.COL, solver.get_cell(3, 5))
        actual_candidates = {(cell.get_row(), cell.get_col()): cell.get_candidates() for cell in modified_cells}
        actual_values = {(cell.get_row(), cell.get_col()): cell.get_value() for cell in modified_cells}

        self.assertEqual(actual_candidates, expected_candidates)
        self.assertEqual(actual_values, expected_values)


if __name__ == '__main__':
    unittest.main()
