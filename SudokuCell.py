
class SudokuCell:
    def __init__(self, row, col, value):
        self.__row = row  # Cannot be modified.
        self.__col = col  # Cannot be modified.
        self.__value = value  # The current digit of this cell.
        self.__candidates = set()  # The set of valid digits for this cell.

    def __str__(self):
        return f"Row: {self.__row}, Col: {self.__col}, Value: {self.__value}, Candidates: {self.__candidates}"

    def get_value(self) -> int:
        return self.__value

    def set_value(self, new) -> None:
        self.__value = new
        self.__candidates.clear()

    def get_candidates(self) -> set:
        return self.__candidates

    def add_candidate(self, candidate: int) -> bool:
        if candidate not in self.__candidates:
            self.__candidates.add(candidate)
            return True
        return False

    def keep_candidates(self, candidates: set) -> None:
        self.__candidates.intersection_update(candidates)

    def remove_candidate(self, candidate: int) -> bool:
        if candidate in self.__candidates:
            self.__candidates.discard(candidate)
            return True
        return False
