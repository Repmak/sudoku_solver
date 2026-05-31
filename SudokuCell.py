
class SudokuCell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value  # The current state of this cell.
        self.candidates = set()  # The set of valid options for this cell.

        self.x_wing_with = set()

    def set_value(self, new):
        self.value = new
        self.candidates.clear()

    def add_candidate(self, candidate: int):
        self.candidates.add(candidate)

    def keep_candidates(self, candidates: set):
        self.candidates.intersection_update(candidates)

    def remove_candidate(self, candidate: int):
        self.candidates.remove(candidate)
