import time
import argparse
import multiprocessing

from gomoku.agent import RandomBot
from gomoku.ruleset import Player, GameState
from gomoku.utils import print_board, print_move


def play_slow(board_size: int, bots) -> Player:
    game = GameState.new_game(board_size)
    while not game.is_over():
        time.sleep(0.2)  

        print(chr(27) + "[2J") 
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)
        print_board(game.board)

    winner = game.winner()
    if winner is None:
        print('Draw')
    else:
        print('{} won the game'.format(winner))
    return winner


def play_fast(board_size: int, bots) -> Player:
    """This can play 4.7 games/sec on 19x19 on MacBook Air"""
    game = GameState.new_game(board_size)
    while not game.is_over():
        bot_move = bots[game.next_player].select_move(game)
        game = game.apply_move(bot_move)
    return game.winner()


def play_games(num_games: int, board_size: int, bots: dict):
    winners = []
    for _ in range(num_games):
        winner = play_fast(board_size, bots)
        winners.append(winner)
    return winners


def play_parallel(num_games: int, board_size: int, bots: dict):
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    winners = pool.starmap(play_fast, [(board_size, bots) for _ in range(num_games)])
    return winners


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--num-games', '-n', type=int, default=100)
    parser.add_argument('--board-size', '-b', type=int, default=19)
    args = parser.parse_args()

    # Prepare bots
    bots = {
        Player.black: RandomBot(),
        Player.white: RandomBot(),
    } 

    # Run games
    start_time = time.time()
    winners = play_parallel(args.num_games, args.board_size, bots)
    total_time = time.time() - start_time

    # Print result
    games_per_second = args.num_games / total_time
    print("Running {} games in {:.2f}s {:.2f} games/sec".format(args.num_games, total_time, games_per_second))
    black_wins = len([x for x in winners if x == Player.black])
    white_wins = len([x for x in winners if x == Player.white])
    print("Black wins: {}, White wins: {}".format(black_wins, white_wins))


if __name__ == '__main__':
    main()