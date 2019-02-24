import unittest

from gomoku.ruleset import Board, GameState, Move, Point
from .oneplane import OnePlaneEncoder


class BoardTest(unittest.TestCase):

    def test_place_stone(self):
        board_size = 9
        game = GameState.new_game(board_size)
        game = game.apply_move(Move.play(Point(3, 3)))
        game = game.apply_move(Move.play(Point(4, 4)))
        encoder = OnePlaneEncoder(board_size)
        encoded_board = encoder.encode(game)

        self.assertEqual((1, board_size, board_size), encoded_board.shape)
        self.assertEqual(0.0, encoded_board[0, 1, 1])
        self.assertEqual(1.0, encoded_board[0, 2, 2])
        self.assertEqual(-1.0, encoded_board[0, 3, 3])


if __name__ == '__main__':
    unittest.main()