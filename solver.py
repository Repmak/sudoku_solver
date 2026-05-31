

class SudokuSolver:
    def __init__(self):
        self.board = [['-' for _ in range(9)] for _ in range(9)]  # The current state of the board.
        self.notes = [[{i for i in range(1, 10)} for _ in range(9)] for _ in range(9)]  # The set of valid options for a cell.

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.board)

    def setup_board(self, givens):
        # Reset board.
        self.board = [['-' for _ in range(9)] for _ in range(9)]
        # Fill in the board with given values.
        for cell in givens:
            self.board[cell[0]][cell[1]] = cell[2]

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

        while not self.is_complete():
            break

        return True

    # --- PUZZLE SOLVING TECHNIQUES ---

    def naked_single(self):
        # One possible remaining candidate for a cell, so fill it.
        pass

    def naked_pair(self):
        #
        pass

    def naked_triple(self):
        #
        pass

    def naked_quad(self):
        #
        pass

    def hidden_single(self):
        #
        pass

    def hidden_pair(self):
        #
        pass

    def hidden_triples(self):
        #
        pass

    def hidden_quad(self):
        #
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
