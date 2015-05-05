from nose.tools import eq_

import gol


def test_blinker():
    board = set([(1, 0), (1, 1), (1, 2)])

    result = gol.next_gen(board)
    eq_(result, set([(2, 1), (1, 1), (0, 1)]))
