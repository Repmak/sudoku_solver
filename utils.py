from HouseNum import HouseNum
from HouseType import HouseType


def get_coords_for_house(house_type: HouseType, house_num: HouseNum) -> list[tuple[int, int]]:
    idx = house_num.value - 1

    if house_type == HouseType.ROW:
        return [(idx, col) for col in range(9)]

    elif house_type == HouseType.COL:
        return [(row, idx) for row in range(9)]

    elif house_type == HouseType.BOX:
        start_row = (idx // 3) * 3
        start_col = (idx % 3) * 3
        return [(start_row + r, start_col + c) for r in range(3) for c in range(3)]

def get_house_coords_for_cell_by_type(house_type: HouseType, row: int, col: int) -> list[tuple[int, int]]:
    if house_type == HouseType.ROW:
        return [(row, c) for c in range(9)]

    elif house_type == HouseType.COL:
        return [(r, col) for r in range(9)]

    elif house_type == HouseType.BOX:
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        return [(start_row + r, start_col + c) for r in range(3) for c in range(3)]


HOUSE_COORDS_MAP = {(ht, hn): get_coords_for_house(ht, hn) for ht in HouseType for hn in HouseNum}
CELL_HOUSE_COORDS_MAP = {(ht, row, col): get_house_coords_for_cell_by_type(ht, row, col) for ht in HouseType for row in range(9) for col in range(9)}
