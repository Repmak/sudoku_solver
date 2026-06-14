import unittest
from solver import SudokuSolver


GIVENS = ""

class TestSum(unittest.TestCase):

    def test_board_not_set_up(self):
        solver = SudokuSolver()
        with self.assertRaises(ValueError):
            solver.solve()

    def test_invalid_givens(self):
        solver = SudokuSolver()
        with self.assertRaises(ValueError):
            solver.setup_board("givens")


    # def board_set_up_board(self):
    #     expected = '''
    #         \n
    #         \n
    #         \n
    #         \n
    #         \n
    #         \n
    #         \n
    #         \n
    #
    #     '''
    #     solver = SudokuSolver()
    #     solver.setup_board(GIVENS)
    #     self.assertEqual(str(solver), expected)


if __name__ == '__main__':
    unittest.main()
