import unittest

from gomoku.utils import print_board
from gomoku.ruleset import Board, GameState, Move, Point, Player 
from gomoku.agent import MinMaxAgent


class MinMaxTest(unittest.TestCase):

    # def test_first_3(self):
    #     """ This takes 60 seconds """
    #     state = GameState.new_game(9)
    #     state = state.apply_move(Move(Point(3, 3)))
    #     state = state.apply_move(Move(Point(2, 1)))
    #     state = state.apply_move(Move(Point(3, 2)))
    #     state = state.apply_move(Move(Point(2, 2)))
    #     state = state.apply_move(Move(Point(3, 4)))
    #     state = state.apply_move(Move(Point(2, 3)))
    #     print_board(state.board)
    #     agent = MinMaxAgent(depth=3)
    #     move = agent.select_move(state)
    #     print(move)
    #     self.assertFalse(state.is_over())

    def test_defend_3(self):
        agent = MinMaxAgent(depth=3)
        state = GameState.new_game(9)
        state = state.apply_move(Move(Point(1, 1)))
        state = state.apply_move(Move(Point(2, 1)))
        state = state.apply_move(Move(Point(1, 2)))
        state = state.apply_move(Move(Point(2, 2)))
        state = state.apply_move(Move(Point(1, 3)))
        state = state.apply_move(Move(Point(2, 3)))
        state = state.apply_move(Move(Point(1, 4)))
        move = agent.select_move(state)
        self.assertEqual(Point(1, 5), move.point)

    def test_defend_2(self):
        agent = MinMaxAgent(depth=2)
        state = GameState.new_game(9)
        state = state.apply_move(Move(Point(1, 1)))
        state = state.apply_move(Move(Point(1, 8)))
        state = state.apply_move(Move(Point(1, 2)))
        state = state.apply_move(Move(Point(2, 7)))
        state = state.apply_move(Move(Point(5, 3)))
        state = state.apply_move(Move(Point(3, 6)))
        state = state.apply_move(Move(Point(7, 4)))
        state = state.apply_move(Move(Point(4, 5)))
        move = agent.select_move(state)
        self.assertEqual(Point(5, 4), move.point)


if __name__ == '__main__':
    unittest.main()