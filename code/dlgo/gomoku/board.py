
from .types import Point, Player


class Board:
    def __init__(self, size: int = 19):
        self._board_size = size
        self._grid = {}

    def place_stone(self, player: Player, point: Point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        self._grid[point] = player

    def is_on_grid(self, point: Point) -> bool:
        return 0 <= point.row < self._board_size and 0 <= point.col < self._board_size

    def get(self, point: Point) -> Player:
        """Return the content of a point on the board.
        Returns None if the point is empty, or a Player if there is a
        stone on that point.
        """
        return self._grid.get(point)

    def __eq__(self, other):
        return isinstance(other, Board) and \
            self._board_size == other._board_size and \
            self._grid == other._grid