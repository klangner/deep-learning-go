from gomoku.agent import RandomBot
from gomoku import ruleset
from gomoku.utils import print_board, print_move
import time


def play_slow(board_size: int):
    game = ruleset.GameState.new_game(board_size)
    bots = {
        ruleset.Player.black: RandomBot(),
        ruleset.Player.white: RandomBot(),
    } 
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

def play_fast(board_size: int):
    """This can play 4.7 games/sec on 19x19 on MacBook Air"""
    game = ruleset.GameState.new_game(board_size)
    bots = {
        ruleset.Player.black: RandomBot(),
        ruleset.Player.white: RandomBot(),
    } 
    while not game.is_over():
        bot_move = bots[game.next_player].select_move(game)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    start_time = time.time()
    ngames = 100
    for _ in range(ngames):
        play_fast(19)
    total_time = time.time() - start_time
    print("Running {} games in {:.2f}s {:.2} games/sec".format(ngames, total_time, ngames/total_time))
