from gomoku.ruleset import GameState, Move


class Agent:

    def select_move(self, game_state: GameState) -> Move:
        raise NotImplementedError()

