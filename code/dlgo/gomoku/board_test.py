import unittest

from .board import Board
from .types import Point, Player 


class BoardTest(unittest.TestCase):

    def test_place_stone(self):
        board = Board(19)
        board.place_stone(Player.black, Point(2, 2))
        self.assertEqual(Player.black, board.get(Point(2, 2)))

    def test_on_grid(self):
        board = Board(9)
        self.assertTrue(board.is_on_grid(Point(0, 8)))
        self.assertFalse(board.is_on_grid(Point(2, -1)))
        self.assertFalse(board.is_on_grid(Point(12, 1)))


if __name__ == '__main__':
    unittest.main()