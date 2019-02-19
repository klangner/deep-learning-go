import copy

from .board import Board
from .types import Player, Move, Point


class GameState:

    def __init__(self, board: Board, next_player: Player, move: Move):
        self._board = board
        self._next_player = next_player
        self._last_move = move

    def apply_move(self, move: Move) -> 'GameState':
        """Return the new GameState after applying the move."""
        next_board = copy.deepcopy(self._board)
        next_board.place_stone(self._next_player, move.point)
        return GameState(next_board, self._next_player.other, move)

    @classmethod
    def new_game(cls, size: int=19) -> 'GameState':
        board = Board(size)
        return GameState(board, Player.black, None)

    def is_valid_move(self, move: Move) -> bool:
        return self._board.get(move.point) is None and not self.is_over()

    def legal_moves(self) -> [Move]:
        moves = []
        for row in range(self._board.num_rows):
            for col in range(self._board.num_cols):
                move = Move(Point(row, col))
                if self._board.get(move.point) is None:
                    moves.append(move)
        return moves

    def is_over(self) -> bool:
        if self._is_winning_move(self._last_move):
            return True
        if len(self.legal_moves()) == 0:
            return True
        return False

    def winner(self) -> Player:
        if self._is_winning_move(self._last_move):
            return self._next_player.other
        return None

    def _is_winning_move(self, move: Move) -> bool:
        if self._has_horizontal_five(move.point):
            return True
        if self._has_vertical_five(move.point):
            return True
        if self._has_backslash_five(move.point):
            return True
        if self._has_slash_five(move.point):
            return True
        return False

    def _has_horizontal_five(self, point: Point) -> bool:
        player = self._board.get(point)
        counter = 1
        col = point.col - 1
        while counter < 5 and self._board.get(Point(point.row, col)) == player:
            counter += 1
            col -= 1
        col = point.col + 1
        while counter < 5 and self._board.get(Point(point.row, col)) == player:
            counter += 1
            col += 1
        return counter == 5

    def _has_vertical_five(self, point: Point) -> bool:
        player = self._board.get(point)
        counter = 1
        row = point.row - 1
        while counter < 5 and self._board.get(Point(row, point.col)) == player:
            counter += 1
            row -= 1
        row = point.row + 1
        while counter < 5 and self._board.get(Point(row, point.col)) == player:
            counter += 1
            row += 1
        return counter == 5

    def _has_backslash_five(self, point: Point) -> bool:
        player = self._board.get(point)
        counter = 1
        row = point.row - 1
        col = point.col - 1
        while counter < 5 and self._board.get(Point(row, col)) == player:
            counter += 1
            row -= 1
            col -= 1
        row = point.row + 1
        col = point.col + 1
        while counter < 5 and self._board.get(Point(row, col)) == player:
            counter += 1
            row += 1
            col += 1
        return counter == 5

    def _has_slash_five(self, point: Point) -> bool:
        player = self._board.get(point)
        counter = 1
        row = point.row + 1
        col = point.col - 1
        while counter < 5 and self._board.get(Point(row, col)) == player:
            counter += 1
            row += 1
            col -= 1
        row = point.row - 1
        col = point.col + 1
        while counter < 5 and self._board.get(Point(row, col)) == player:
            counter += 1
            row -= 1
            col += 1
        return counter == 5