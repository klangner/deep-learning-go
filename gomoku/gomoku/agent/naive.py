import random

from .base import Agent

from gomoku.ruleset import GameState, Move


class RandomBot(Agent):

    def select_move(self, game_state: GameState) -> Move:
        """Choose a random valid move."""
        candidates = game_state.legal_moves()
        if not candidates:
            return Move.pass_turn()
        return random.choice(candidates)
