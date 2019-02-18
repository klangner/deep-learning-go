import enum
import typing


class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white


class Point(typing.NamedTuple):
    row: int
    col: int


class Move:
    def __init__(self, point: Point):
        self.point = point