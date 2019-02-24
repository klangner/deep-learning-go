import argparse
import numpy as np

from gomoku.encoders.base import get_encoder_by_name
from gomoku.ruleset import GameState
from gomoku.agent import MCTSAgent
from gomoku.utils import print_board, print_move


def generate_game(board_size: int, rollout: int, temperature: float):
    boards, moves = [], []
    
    encoder = get_encoder_by_name('oneplane', board_size)

    game = GameState.new_game(board_size)

    bot = MCTSAgent(rollout, temperature)

    while not game.is_over():
        # print_board(game.board)
        move = bot.select_move(game)
        if move.is_play:
            boards.append(encoder.encode(game))
            move_one_hot = np.zeros(encoder.num_points())
            move_one_hot[encoder.encode_point(move.point)] = 1
            moves.append(move_one_hot)

        # print_move(game.next_player, move)
        game = game.apply_move(move)

    return np.array(boards), np.array(moves)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--board-size', '-s', type=int, default=9)
    parser.add_argument('--rollouts', '-r', type=int, default=1000)
    parser.add_argument('--temperature', '-t', type=float, default=0.8)
    parser.add_argument('--num-games', '-n', type=int, default=10)
    parser.add_argument('--board-out')
    parser.add_argument('--move-out')

    args = parser.parse_args() 
    xs = []
    ys = []

    for i in range(args.num_games):
        print('Generating game %d/%d...' % (i + 1, args.num_games))
        x, y = generate_game(args.board_size, args.rollouts, args.temperature) 
        xs.append(x)
        ys.append(y)

    x = np.concatenate(xs) 
    y = np.concatenate(ys)

    np.save(args.board_out, x)
    np.save(args.move_out, y)


if __name__ == '__main__':
    main()
