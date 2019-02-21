import argparse
import pickle

from gomoku.ruleset import GameState
from gomoku.utils import print_game_state




def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='GameState pickle')
    args = parser.parse_args()
    
    file = open(args.file, mode='rb')
    game_state = pickle.load(file)
    file.close()
    print_game_state(game_state)


if __name__ == '__main__':
    main()