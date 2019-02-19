import copy
import numpy as np
from debug import total_size

from dlgo.gotypes import Player, Point


def size_of_numpy_array(nplay=200):
    np_game_record = []
    for _ in range(200):
        a = np.array([Player.black for _ in range(19*19)])
        np_game_record.append(a)
    print('Numpy array: {} KB'.format(total_size(np_game_record) // 1024))


def size_of_dict(nplay=200):
    grids = []
    grid = {}
    for i in range(200):
        grid[Point(i, i)] = Player.black
        grids.append(grid)
        grid = copy.copy(grid)
    print('Dict: {} KB'.format(total_size(grid) // 1024))


if __name__ == '__main__':
    size_of_numpy_array()
    size_of_dict()
