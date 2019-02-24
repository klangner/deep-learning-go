import numpy as np 

from gomoku.encoders.base import Encoder
from gomoku.ruleset import Point, GameState


class OnePlaneEncoder(Encoder):
    def __init__(self, board_size: int):
        self.board_size = board_size
        self.num_planes = 1

    def name(self):
        return 'oneplane'

    def encode(self, game_state: GameState) -> 'np.array':
        board_matrix = np.zeros(self.shape())
        next_player = game_state.next_player
        for r in range(self.board_size):
            for c in range(self.board_size):
                p = Point(row=r + 1, col=c + 1)
                player = game_state.board.get(p)
                if player is None:
                    continue
                elif player == next_player:
                    board_matrix[0, r, c] = 1
                else:
                    board_matrix[0, r, c] = -1
        return board_matrix

    def encode_point(self, point: Point) -> int:
        return self.board_size * (point.row - 1) + (point.col - 1)

    def decode_point_index(self, index: int) -> Point:
        row = index // self.board_size
        col = index % self.board_size
        return Point(row=row + 1, col=col + 1)

    def num_points(self) -> int:
        return self.board_size * self.board_size

    def shape(self):
        return self.num_planes, self.board_size, self.board_size


def create(board_size: int) -> Encoder:
    return OnePlaneEncoder(board_size)