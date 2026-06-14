import itertools
from collections import deque, defaultdict
from functools import reduce
from typing import overload, Optional

from SudokuCell import SudokuCell, EMPTY_CELL
from HouseNum import HouseNum
from HouseType import HouseType
from utils import HOUSE_COORDS_MAP, CELL_HOUSE_COORDS_MAP


class SudokuSolver:
    def __init__(self):
        self._board = []
        self._setup_complete = False

    def __str__(self):
        return "\n".join([" ".join([str(cell.get_value() if not cell.is_empty() else " ") for cell in row]) for row in self._board])

    def get_board(self):
        return self._board

    def setup_board(self, givens: str) -> None:
        if len(givens) != 81: raise ValueError("Invalid board state.")
        self._board = [[SudokuCell(row, col) for col in range(9)] for row in range(9)]  # Reset board.

        # Fill in the board with given values.
        for i, char in enumerate(givens):
            if not (char == '.' or char == ' ' or char == '0'):
                self._board[i // 9][i % 9].set_value(int(char))
                # Remove this value from the candidates of other cells in the given's house.
                candidate_to_remove = {int(char)}
                for ht in HouseType:
                    for row, col in CELL_HOUSE_COORDS_MAP[(ht, i // 9, i % 9)]:
                        self._board[row][col].remove_candidates(candidate_to_remove)

        self._setup_complete = True  # solve() can be called now.

    def is_complete(self):
        to_compare = {i for i in range(1, 10)}

        for ht in HouseType:
            for hn in HouseNum:
                seen = set()

                for row, col in HOUSE_COORDS_MAP[(ht, hn)]:
                    val = self._board[row][col].get_value()
                    if self._board[row][col] in seen: return False
                    seen.add(val)

                if seen != to_compare: return False

        return True

    def solve(self) -> bool:
        if not self._setup_complete: raise ValueError("Board setup not complete.")

        while not self.is_complete():
            '''
            This queue will be used to store SudokuCell instances that have been modified when applying solving
            techniques. These need to be checked to see if the alterations propagate to finding new cell values.
            '''
            queue = deque()
            queue_set = set()  # To avoid adding a cell already present in the queue again.

            while queue:
                dirty_cell = queue.popleft()
                queue_set.remove(dirty_cell)

                # First attempt to use logic.

                # Fallback on using search (i.e. backtracking) if required.

            print(self)
            break

        return True

    # --- PUZZLE SOLVING TECHNIQUE HELPERS ---



    # --- PUZZLE SOLVING TECHNIQUES ---

    def fill_cell(self, cell: SudokuCell) -> bool:
        if cell.get_candidate_count() > 1: return False  # Exit if the cell has more than one candidate.
        for ht in HouseType:
            for row, col in CELL_HOUSE_COORDS_MAP[(ht, cell.get_row(), cell.get_col())]:
                if self._board[row][col] != cell:
                    self._board[row][col].remove_candidates(cell.get_candidates())
        cell.set_value(list(cell.get_candidates())[0])

    @overload
    def naked_subset(self, house_num: HouseNum, house_type: HouseType) -> set[SudokuCell]: ...
    @overload
    def naked_subset(self, cell: SudokuCell) -> set[SudokuCell]: ...
    @overload
    def naked_subset(self, house_type: HouseType, cell: SudokuCell) -> set[SudokuCell]: ...

    def naked_subset(
        self,
        house_num: Optional[HouseNum] = None,
        house_type: Optional[HouseType] = None,
        cell: SudokuCell = None
    ) -> set[SudokuCell]:
        """
        Implementation for the naked subset technique.

        A naked single occurs when a cell that has a single candidate number remaining.
        A naked pair occurs when 2 cells in a house share the same 2 candidates.
        A naked triple occurs when 3 cells in a house share the same 3 candidates.
        Etc.

        :param house_num: To identify the house to search.
        :param house_type: To identify the house to search.
        :param cell: To identify the houses of the cell to search.
        :return: The cell(s) whose candidates have been modified as a consequence of finding a distinct set of cells which form a naked subset.
        """
        if house_num is not None and house_type is not None and cell is None:
            # First overload.
            empty_cells = {
                self._board[row][col]
                for row, col in HOUSE_COORDS_MAP[(house_num, house_type)]
                if self._board[row][col].is_empty()
            }
            already_used_cells = set()  # Cells that have been added to a naked subset.
            modified_cells = set()  # Cells whose candidates have been modified as a consequence of finding a naked subset.

            # Iterate through the subset sizes.
            for subset_size in range(2, 5):
                # Iterate through the combinations of cell subsets that can be formed for a given size.
                for subset_tuple in itertools.combinations(empty_cells, subset_size):
                    subset = set(subset_tuple)

                    # Skip over cells that have previously been matched in a naked subset.
                    if any(c in already_used_cells for c in subset):
                        continue

                    # Check if len(union of candidates across the subset) == subset_size.
                    union_of_candidates = reduce(lambda x, y: x.union(y),
                                                 [subset_cell.get_candidates() for subset_cell in subset])
                    if len(union_of_candidates) == subset_size:
                        print(f'Found naked subset (cells: {"; ".join([str(c) for c in subset])}).')
                        already_used_cells.update(subset)

                        # Remove the candidates in the other cells.
                        for other_cell in empty_cells - subset:
                            if other_cell.remove_candidates(union_of_candidates):
                                modified_cells.add(other_cell)

            return modified_cells

        elif house_num is None and house_type is None and cell is not None:
            # Second overload.
            return self.naked_subset(HouseType.ROW, cell).union(
                self.naked_subset(HouseType.COL, cell), self.naked_subset(HouseType.BOX, cell))

        elif house_num is None and house_type is not None and cell is not None:
            # Third overload.
            empty_cells = {
                self._board[row][col]
                for row, col in CELL_HOUSE_COORDS_MAP[(house_type, cell.get_row(), cell.get_col())]
                if self._board[row][col].is_empty() and self._board[row][col] != cell  # Note that the cell param is excluded, but will be added later.
            }
            modified_cells = set()  # Cells whose candidates have been modified as a consequence of finding a naked subset.

            # Iterate through the subset sizes.
            for subset_size in range(2, 5):
                # Iterate through the combinations of subsets that can be formed for a given size.
                for subset_tuple_excluding_cell in itertools.combinations(empty_cells, subset_size - 1): # Subset size is reduced by 1 since the cell param is added to the subset later.
                    cell_subset = set(subset_tuple_excluding_cell) | {cell}

                    # Check if len(union of candidates across the subset) == subset_size.
                    union_of_candidates = reduce(lambda x, y: x.union(y),
                                                 [subset_cell.get_candidates() for subset_cell in cell_subset])
                    if len(union_of_candidates) == subset_size:
                        print(f'Found naked subset (cells: {"; ".join([str(c) for c in cell_subset])}).')

                        # Remove the candidates in the other cells.
                        for other_cell in empty_cells - cell_subset:
                            if other_cell.remove_candidates(union_of_candidates):
                                modified_cells.add(other_cell)
                        return modified_cells  # Return early once the cell param gets matched to a naked subset.

            return modified_cells  # This should always return an empty set.

        else: raise ValueError('Invalid params for method naked_subset.')

    @overload
    def hidden_subset(self, house_num: HouseNum, house_type: HouseType) -> set[SudokuCell]: ...
    @overload
    def hidden_subset(self, cell: SudokuCell) -> set[SudokuCell]: ...
    @overload
    def hidden_subset(self, house_type: HouseType, cell: SudokuCell) -> set[SudokuCell]: ...

    def hidden_subset(
        self,
        house_num: Optional[HouseNum] = None,
        house_type: Optional[HouseType] = None,
        cell: SudokuCell = None
    ) -> set[SudokuCell]:
        """
        Implementation for the hidden subset technique.

        A hidden single occurs when a candidate appears only once in a house.
        A hidden pair occurs when 2 candidates appear within the same 2 cells of a house.
        A hidden triple occurs when 3 candidates appear within the same 3 cells of a house.
        Etc.

        :param house_num: To identify the house to search.
        :param house_type: To identify the house to search.
        :param cell: To identify the houses of the cell to search.
        :return: The cell(s) whose candidates have been modified as a consequence of finding a distinct set of cells which form a hidden subset.
        """

        if house_num is not None and house_type is not None and cell is None:
            # First overload.
            candidates_to_cell_map = defaultdict(set)
            for row, col in HOUSE_COORDS_MAP[(house_type, house_num)]:
                if self._board[row][col].is_empty():
                    for candidate in self._board[row][col].get_candidates():
                        candidates_to_cell_map[candidate].add(self._board[row][col])

            house_candidates = candidates_to_cell_map.keys()
            already_used_cells = set()  # Cells that have been added to a hidden subset.
            already_used_candidates = set()  # Candidates that have been used to form a hidden subset.
            modified_cells = set()  # Cells whose candidates have been modified as a consequence of finding a naked subset.

            # Iterate through the subset sizes.
            for subset_size in range(2, 5):
                # Iterate through the combinations of candidate subsets that can be formed for a given size.
                for candidate_subset_tuple in itertools.combinations(house_candidates, subset_size):
                    candidate_subset = set(candidate_subset_tuple)

                    # Skip if this combination includes a candidate that is part of a hidden subset.
                    if candidate_subset & already_used_candidates: continue

                    # Try to find subset_size empty cells that form a hidden subset.
                    hidden_subset_cells = set()
                    for candidate in candidate_subset:
                        hidden_subset_cells.update(candidates_to_cell_map[candidate])
                    hidden_subset_cells -= already_used_cells

                    if len(hidden_subset_cells) == subset_size:
                        for c in hidden_subset_cells:
                            already_used_cells.add(c)
                            if c.keep_candidates(candidate_subset):
                                modified_cells.add(c)
                        already_used_candidates.update(candidate_subset)

            return modified_cells

        elif house_num is None and house_type is None and cell is not None:
            # Second overload.
            return self.hidden_subset(HouseType.ROW, cell).union(
                self.hidden_subset(HouseType.COL, cell), self.hidden_subset(HouseType.BOX, cell))

        elif house_num is None and house_type is not None and cell is not None:
            # Third overload.
            candidates_to_cell_map = defaultdict(set)
            for row, col in CELL_HOUSE_COORDS_MAP[(house_type, cell.get_row(), cell.get_col())]:
                if self._board[row][col].is_empty():
                    for candidate in self._board[row][col].get_candidates():
                        candidates_to_cell_map[candidate].add(self._board[row][col])

            house_candidates = candidates_to_cell_map.keys()
            modified_cells = set()  # Cells whose candidates have been modified as a consequence of finding a hidden subset.

            # Iterate through the subset sizes.
            for subset_size in range(2, max(5, cell.get_candidate_count() + 1)):
                # Iterate through the combinations of candidate subsets that can be formed for a given size.
                for candidate_subset_tuple in itertools.combinations(house_candidates, subset_size):
                    candidate_subset = set(candidate_subset_tuple)

                    # Skip if the cell param does not have any candidates in common with candidate_subset.
                    if not (candidate_subset & cell.get_candidates()): continue

                    # Try to find subset_size empty cells (including the cell param) that form a hidden subset.
                    hidden_subset_cells = set()
                    for candidate in candidate_subset:
                        hidden_subset_cells.update(candidates_to_cell_map[candidate])

                    if len(hidden_subset_cells) == subset_size:
                        if len(hidden_subset_cells) == subset_size:
                            for c in hidden_subset_cells:
                                if c.keep_candidates(candidate_subset):
                                    modified_cells.add(c)
                        return modified_cells  # Return early once the cell param gets matched to a hidden subset.

            return modified_cells  # This should always return an empty set.

        else: raise ValueError('Invalid params for method hidden_subset.')

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
