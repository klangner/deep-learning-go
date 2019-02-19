from gomoku.agent import RandomBot
from gomoku import ruleset
from gomoku.utils import print_board, print_move
import time


def main():
    board_size = 19
    game = ruleset.GameState.new_game(board_size)
    bots = {
        ruleset.Player.black: RandomBot(),
        ruleset.Player.white: RandomBot(),
    } 
    while not game.is_over():
        time.sleep(0.01)  

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

if __name__ == '__main__':
    main()
