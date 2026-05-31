from typing import overload, Optional

from SudokuCell import SudokuCell
from HouseNum import HouseNum
from HouseType import HouseType

class SudokuSolver:
    def __init__(self):
        self.board = []  # The current state of the board.
        self.setup_complete = False

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.board)

    def setup_board(self, givens):
        # Reset board.
        self.board = [[SudokuCell(row, col, '-') for col in range(9)] for row in range(9)]
        # Fill in the board with given values.
        for cell in givens:
            self.board[cell[0]][cell[1]] = cell[2]
        # solve() can be called now.
        self.setup_complete = True

    def is_complete(self):
        to_compare = {i for i in range(1, 10)}
        for i in range(9):
            seen_row = set()
            seen_col = set()
            seen_box = set()

            for j in range(9):
                if self.board[i][j] in seen_row: return False
                seen_row.add(self.board[i][j])
            if seen_row != to_compare: return False

            for j in range(9):
                if self.board[j][i] in seen_col: return False
                seen_col.add(self.board[j][i])
            if seen_col != to_compare: return False

            box_row_start = (i // 3) * 3
            box_col_start = (i % 3) * 3
            for j in range(9):
                row_idx = box_row_start + (j // 3)
                col_idx = box_col_start + (j % 3)
                if self.board[row_idx][col_idx] in seen_box: return False
                seen_box.add(self.board[row_idx][col_idx])
            if seen_box != to_compare: return False

        return True

    def solve(self):
        if not self.setup_complete: return False

        while not self.is_complete():

            print(self)
            break

        return True

    # --- PUZZLE SOLVING TECHNIQUES ---

    @overload
    def naked_n(self, n: int) -> None: ...

    @overload
    def naked_n(self, n: int, house_num: HouseNum, house_type: HouseType) -> None: ...

    def naked_n(self, n: int, house_num: Optional[HouseNum] = None, house_type: Optional[HouseType] = None):
        """
        Implementation for the naked subset technique.

        A naked single occurs when a cell that has a single candidate number remaining.
        A naked pair occurs when 2 cells in a house share the same 2 candidates.
        A naked triple occurs when 3 cells in a house share the same 3 candidates.
        Etc.

        :param n: The size of the naked set of candidates.
        :param house_num:
        :param house_type:
        :return:
        """
        if house_num is None and house_type is None:
            # Aimlessly search for a naked set.
            return

        # Only 1 possible candidate for a cell.
        for i in range(9):
            pass

    # @overload
    # def naked_single(self) -> None: ...
    # @overload
    # def naked_single(self, house_num: HouseNum, house_type: HouseType) -> None: ...
    # def naked_single(self, house_num: Optional[HouseNum] = None, house_type: Optional[HouseType] = None):
    #     if house_num is None and house_type is None:
    #         # Aimlessly search for a naked single
    #         return
    #
    #     # Only 1 possible candidate for a cell.
    #     for i in range(9):
    #         pass
    #
    # def naked_pair(self):
    #     # 2 possible candidates across 2 cells.
    #     pass
    #
    # def naked_triple(self):
    #     # 3 possible candidates across 3 cells.
    #     pass
    #
    # def naked_quad(self):
    #     #
    #     pass

    @overload
    def hidden_n(self, n: int) -> None: ...

    @overload
    def hidden_n(self, n: int, house_num: HouseNum, house_type: HouseType) -> None: ...

    def hidden_n(self, n: int, house_num: Optional[HouseNum] = None, house_type: Optional[HouseType] = None):
        """
        Implementation for the hidden subset technique.

        A hidden single occurs when a candidate appears only once in a house.
        A hidden pair occurs when 2 candidates appear within the same 2 cells of a house.
        A hidden triple occurs when 3 candidates appear within the same 3 cells of a house.
        Etc.

        :param n: The size of the hidden set of candidates.
        :param house_num:
        :param house_type:
        :return:
        """
        if house_num is None and house_type is None:
            # Aimlessly search for a hidden set.
            return

        for i in range(9):
            pass

    def pointing_pairs(self):
        #
        pass

    def pointing_triples(self):
        #
        pass

    def x_wing(self):
        #
        pass

    def swordfish(self):
        #
        pass

    def jellyfish(self):
        #
        pass

    def xy_wing(self):
        #
        pass

    def xyz_wing(self):
        #
        pass
