from nose.tools import eq_

import sudoku


def check_valid_board(board):
    for row in board:
        pass


def test_check_valid_board():
    pass


def test_create_board():
    eq_(sudoku.create_board(), [[0] * 9] * 9)


def test_valid_for_row():
    eq_(sudoku.valid_for_row([], 1), True)


def test_valid_for_row_number_already_exists():
    eq_(sudoku.valid_for_row([1], 1), False)


def test_valid_for_column():
    eq_(sudoku.valid_for_column([], 1), True)


def test_valid_for_block():
    eq_(sudoku.valid_for_block([], 1), True)


def test_extract_column():
    eq_(sudoku.extract_column([[1] + [0] * 8] * 9, 0), [1] * 9)


def test_available_numbers_none():
    eq_(sudoku.available_numbers(range(1, 10)), [])


def test_available_numbers_all():
    eq_(sudoku.available_numbers([]), range(1, 10))


def test_available_numbers_some():
    eq_(sudoku.available_numbers(range(1, 5)), range(5, 10))


def test_find_block_index():
    eq_(sudoku.find_block_index(5, 5), (1, 1))


def test_extract_block():
    eq_(sudoku.extract_block([[1] + [0] * 8] * 9, 0, 0), [1, 0, 0] * 3)
