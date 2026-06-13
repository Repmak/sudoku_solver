
EMPTY_CELL = 0

class SudokuCell:
    def __init__(self, row, col, value=EMPTY_CELL):
        self._row = row  # Cannot be modified.
        self._col = col  # Cannot be modified.
        self._value = value  # The current digit of this cell.
        self._candidates = set()  # The set of valid digits for this cell.

    def __str__(self):
        return f"R{self._row + 1}C{self._col + 1}), Value: {self._value}" \
            if self._value else f"R{self._row + 1}C{self._col + 1}), Candidates: {self._candidates}"

    def get_row(self):
        return self._row

    def get_col(self):
        return self._col

    def get_value(self) -> int:
        return self._value

    def is_empty(self) -> int:
        return self._value == EMPTY_CELL

    def set_value(self, new) -> None:
        self._value = new
        self._candidates.clear()

    def get_candidates(self) -> set[int]:
        return self._candidates

    def get_candidate_count(self) -> int:
        return len(self._candidates)

    def has_candidates(self, candidates: set[int]) -> bool:
        return candidates.issubset(self._candidates)

    def add_candidate(self, candidate: int) -> bool:
        if candidate in self._candidates:
            # The candidate is already present.
            # Selection statement not needed for safety, just to satisfy returning a boolean.
            return False
        self._candidates.add(candidate)
        return True

    def keep_candidates(self, candidates: set[int]) -> bool:
        if self._candidates.issubset(candidates):
            # These candidates are not present (so the resulting self._candidates would be empty).
            return False
        self._candidates.intersection_update(candidates)
        return True

    def remove_candidates(self, candidates: set[int]) -> bool:
        if len(candidates) == 0 or self._candidates.isdisjoint(candidates):
            # None of the candidates are present. There is nothing to remove.
            return False
        self._candidates -= candidates
        return True
