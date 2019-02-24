import cProfile
import argparse
import time

from gomoku.ruleset import GameState
from gomoku.agent import MinMaxAgent, MCTSAgent


def measure_move_time(agent):
    game_state = GameState.new_game(9)    
    start_time = time.time()
    agent.select_move(game_state)
    total_time = time.time() - start_time
    print('Finished in {:.2f}sec.'.format(total_time))

def main():
    measure_move_time(MinMaxAgent(depth=3))
    # measure_move_time(MCTSAgent(10000))

if __name__ == '__main__':
    main()