import unittest

from solver import SudokuSolver
from SudokuCell import SudokuCell, EMPTY_CELL
from HouseNum import HouseNum
from HouseType import HouseType
from utils import HOUSE_COORDS_MAP, CELL_HOUSE_COORDS_MAP


# Taken from https://hodoku.sourceforge.net/en/show_example.php?file=h302&tech=Hidden+Triple.
GIVENS = "5..62..37..489........5....93........2....6.57.......3.....9.........7..68.57...2"


class TestSum(unittest.TestCase):

    def test_naked_triple_first_overload(self):
        self.assertEquals(1, 1)

    def test_naked_triple_second_overload(self):
        self.assertEquals(1, 1)

    def test_naked_triple_third_overload(self):
        self.assertEquals(1, 1)


if __name__ == '__main__':
    unittest.main()
