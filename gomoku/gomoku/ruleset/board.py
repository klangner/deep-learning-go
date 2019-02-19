import copy

from .types import Point, Player


class Board:
    def __init__(self, size: int = 19):
        self.num_rows = size
        self.num_cols = size
        self._grid = {}

    def place_stone(self, player: Player, point: Point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        self._grid[point] = player

    def is_on_grid(self, point: Point) -> bool:
        return 1 <= point.row <= self.num_rows and 1 <= point.col <= self.num_cols

    def get(self, point: Point) -> Player:
        """Return the content of a point on the board.
        Returns None if the point is empty, or a Player if there is a
        stone on that point.
        """
        return self._grid.get(point)

    def __eq__(self, other):
        return isinstance(other, Board) and \
            self.num_rows == other.num_rows and \
            self.num_cols == other.num_cols and \
            self._grid == other._grid

    def __deepcopy__(self, memodict={}):
        copied = Board(self.num_rows)
        copied._grid = copy.copy(self._grid)
        return copied