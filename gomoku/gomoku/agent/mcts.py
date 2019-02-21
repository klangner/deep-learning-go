import random
import math

from .base import Agent
from .naive import RandomAgent

from gomoku.ruleset import GameState, Move, Player


class MCTSAgent(Agent):
    def __init__(self, num_rounds: int, temperature: float=1.5):
        """
        temperature = 'c' parameter in UCT formula (Upper Confidence Bounds for Trees)
        """
        self.num_rounds = num_rounds
        self.temperature = temperature

    def select_move(self, game_state: GameState) -> Move:
        # Calculate winning probability
        root = MCTSNode(game_state)
        for _ in range(self.num_rounds):
            node = root
            # Try to find a node where we can add new child
            while (not node.can_add_child()) and (not node.is_terminal()):
                node = self.select_child(node)
            if node.can_add_child():
                node = node.add_random_child()
            # simulate random outcome from this node
            winner = self.simulate_random_game(node.game_state)
            # Propagate winning up to the root
            while node is not None:
                node.record_win(winner)
                node = node.parent
        # Select best move
        best_move = None
        best_pct = -1.0
        for child in root.children:
            child_pct = child.winning_frac(game_state.next_player)
            if child_pct > best_pct:
                best_pct = child_pct
                best_move = child.move
        return best_move

    def select_child(self, node):
        """ Use UCT formula to select node to explore
        uct = w + c * sqrt(log N / n)
        where:
            w - winning fraction for given node
            c - exploitation vs exploration factor (temperature)
            N - Number of rollouts
            n - Number of rollouts for given child
        """
        total_rollouts = sum(child.num_rollouts for child in node.children)
        log_rollouts = math.log(total_rollouts)
        best_score = -1
        best_child = -1
        for child in node.children:
            win_percentage = child.winning_frac(node.game_state.next_player)
            exploration_factor = math.sqrt(log_rollouts / child.num_rollouts)
            uct_score = win_percentage + self.temperature * exploration_factor
            # Check if this is the largest we've seen so far.
            if uct_score > best_score:
                best_score = uct_score
                best_child = child
        return best_child

    @staticmethod
    def simulate_random_game(game):
        bots = { 
            Player.black: RandomAgent(),
            Player.white: RandomAgent(),
        }
        while not game.is_over():
            bot_move = bots[game.next_player].select_move(game)
            game = game.apply_move(bot_move)
        return game.winner()


class MCTSNode:

    def __init__(self, game_state: GameState, parent:'MCTSNode'=None, move: Move=None):
        self.game_state = game_state
        self.parent = parent
        self.move = move
        self.win_counts = {
            Player.black: 0,
            Player.white: 0,
        }
        self.num_rollouts = 0
        self.children = []
        self.unvisited_moves = game_state.legal_moves()

    def add_random_child(self) -> 'MCTSNode':
        """Select random unvisited move and create SubNode for it
        """
        index = random.randint(0, len(self.unvisited_moves) - 1)
        new_move = self.unvisited_moves.pop(index)
        new_game_state = self.game_state.apply_move(new_move)
        new_node = MCTSNode(new_game_state, self, new_move)
        self.children.append(new_node)
        return new_node

    def record_win(self, winner):
        if winner is not None:
            self.win_counts[winner] += 1
        self.num_rollouts += 1

    def can_add_child(self):
        return len(self.unvisited_moves) > 0

    def is_terminal(self):
        return self.game_state.is_over()

    def winning_frac(self, player):
        return float(self.win_counts[player]) / float(self.num_rollouts)
    

