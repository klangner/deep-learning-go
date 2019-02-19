import unittest

from .gamestate import GameState
from .board import Board
from .types import Point, Player, Move


class GameStateTest(unittest.TestCase):

    def test_new_game(self):
        state = GameState.new_game(19)
        next_state = state.apply_move(Move(Point(2, 2)))
        board = next_state.board
        self.assertEqual(Player.black, board.get(Point(2, 2)))

    def test_validate_move(self):
        state = GameState.new_game(19)
        next_state = state.apply_move(Move(Point(2, 2)))
        self.assertFalse(next_state.is_valid_move(Move(Point(2, 2))))
        self.assertTrue(next_state.is_valid_move(Move(Point(1, 1))))

    def test_legal_move(self):
        state = GameState.new_game(10)
        next_state = state.apply_move(Move(Point(2, 2)))
        legal_moves = next_state.legal_moves()
        self.assertEqual(99, len(legal_moves))

    def test_is_over_h(self):
        state = GameState.new_game(9)
        state = state.apply_move(Move(Point(1, 1)))
        state = state.apply_move(Move(Point(2, 1)))
        state = state.apply_move(Move(Point(1, 2)))
        state = state.apply_move(Move(Point(2, 2)))
        state = state.apply_move(Move(Point(1, 3)))
        state = state.apply_move(Move(Point(2, 3)))
        state = state.apply_move(Move(Point(1, 4)))
        self.assertFalse(state.is_over())
        state = state.apply_move(Move(Point(2, 4)))
        self.assertFalse(state.is_over())
        state = state.apply_move(Move(Point(1, 5)))
        self.assertTrue(state.is_over())

    def test_is_over_v(self):
        state = GameState.new_game(9)
        state = state.apply_move(Move(Point(3, 3)))
        state = state.apply_move(Move(Point(2, 1)))
        state = state.apply_move(Move(Point(4, 3)))
        state = state.apply_move(Move(Point(2, 2)))
        state = state.apply_move(Move(Point(5, 3)))
        state = state.apply_move(Move(Point(2, 3)))
        state = state.apply_move(Move(Point(6, 3)))
        self.assertFalse(state.is_over())
        state = state.apply_move(Move(Point(2, 4)))
        self.assertFalse(state.is_over())
        state = state.apply_move(Move(Point(7, 3)))
        self.assertTrue(state.is_over())

    def test_is_over_backslash(self):
        state = GameState.new_game(9)
        state = state.apply_move(Move(Point(3, 3)))
        state = state.apply_move(Move(Point(2, 1)))
        state = state.apply_move(Move(Point(4, 4)))
        state = state.apply_move(Move(Point(2, 2)))
        state = state.apply_move(Move(Point(5, 5)))
        state = state.apply_move(Move(Point(2, 3)))
        state = state.apply_move(Move(Point(6, 6)))
        self.assertFalse(state.is_over())
        state = state.apply_move(Move(Point(2, 4)))
        self.assertFalse(state.is_over())
        state = state.apply_move(Move(Point(7, 7)))
        self.assertTrue(state.is_over())

    def test_is_over_slash(self):
        state = GameState.new_game(9)
        state = state.apply_move(Move(Point(8, 3)))
        state = state.apply_move(Move(Point(2, 1)))
        state = state.apply_move(Move(Point(7, 4)))
        state = state.apply_move(Move(Point(2, 2)))
        state = state.apply_move(Move(Point(6, 5)))
        state = state.apply_move(Move(Point(2, 3)))
        state = state.apply_move(Move(Point(5, 6)))
        self.assertFalse(state.is_over())
        state = state.apply_move(Move(Point(2, 4)))
        self.assertFalse(state.is_over())
        state = state.apply_move(Move(Point(4, 7)))
        self.assertTrue(state.is_over())

    def test_winner(self):
        state = GameState.new_game(9)
        state = state.apply_move(Move(Point(8, 3)))
        state = state.apply_move(Move(Point(2, 1)))
        state = state.apply_move(Move(Point(7, 4)))
        state = state.apply_move(Move(Point(2, 2)))
        state = state.apply_move(Move(Point(6, 5)))
        state = state.apply_move(Move(Point(2, 3)))
        state = state.apply_move(Move(Point(5, 6)))
        self.assertIs(None, state.winner())
        state = state.apply_move(Move(Point(2, 4)))
        self.assertIs(None, state.winner())
        state = state.apply_move(Move(Point(4, 7)))
        self.assertIs(Player.black, state.winner())


if __name__ == '__main__':
    unittest.main()