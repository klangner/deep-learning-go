import argparse
import time

from gomoku.ruleset import GameState
from gomoku.agent import MinMaxAgent


def measure_move_time(depth=1):
    game_state = GameState.new_game(9)    
    agent = MinMaxAgent(depth=depth)
    start_time = time.time()
    agent.select_move(game_state)
    total_time = time.time() - start_time
    print('Depth {}. Finished in {:.2f}sec.'.format(depth, total_time))

def main():
    measure_move_time(1)
    measure_move_time(2)
    measure_move_time(3)

if __name__ == '__main__':
    main()