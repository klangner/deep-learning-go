import random

from .base import Agent

from gomoku.ruleset import GameState, Move


class MinMaxAgent(Agent):

    def __init__(self, depth=1):
        self._depth = depth

    def select_move(self, game_state: GameState) -> Move:
        """Choose a random valid move."""
        move, value = self.move_value(game_state, self._depth)
        print('{:} {:}'.format(move, value))
        return move

    def move_value(self, game_state: GameState, depth: int) -> (Move, int):
        candidates = game_state.legal_moves()
        if not candidates:
            return (Move.pass_turn(), 0)
        for move in candidates:
            next_state = game_state.apply_move(move)
            if next_state.is_over():
                return (move, 1)
        if depth > 1:
            best_move, best_value = random.choice(candidates), -1
            for move in candidates:
                next_state = game_state.apply_move(move)
                _, value = self.move_value(next_state, depth-1)
                value *= -1
                if value > best_value:
                    best_move = move
                    best_value = value
            return (best_move, best_value)
        return random.choice(candidates), 0

