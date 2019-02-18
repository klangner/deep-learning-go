from .board import Board
from .types import Player


class GameState:
    def __init__(self, board: Board, next_player: Player):
        self._board = board
        self._next_player = next_player