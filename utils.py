from HouseNum import HouseNum
from HouseType import HouseType


def get_house_cell_coords(house_type: HouseType, house_num: HouseNum) -> list[tuple[int, int]]:
    idx = house_num.value - 1

    if house_type == HouseType.ROW:
        return [(idx, col) for col in range(9)]

    elif house_type == HouseType.COL:
        return [(row, idx) for row in range(9)]

    elif house_type == HouseType.BOX:
        start_row = (idx // 3) * 3
        start_col = (idx % 3) * 3
        return [(start_row + r, start_col + c) for r in range(3) for c in range(3)]


HOUSE_CELL_COORD_MAP = {(ht, hn): get_house_cell_coords(ht, hn) for ht in HouseType for hn in HouseNum}
