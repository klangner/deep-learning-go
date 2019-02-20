import random

from .base import Agent

from gomoku.ruleset import GameState, Move


class MinMaxAgent(Agent):

    def select_move(self, game_state: GameState) -> Move:
        """Choose a random valid move."""
        candidates = game_state.legal_moves()
        # Pass if not valid moves left
        if not candidates:
            return Move.pass_turn()
        # Find winning move if possible
        for move in candidates:
            next_state = game_state.apply_move(move)
            if next_state.is_over():
                return move
        # Just random move
        return random.choice(candidates)
