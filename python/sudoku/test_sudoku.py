from nose.tools import eq_

import sudoku


def valid_seq(seq):
    return len(set(seq)) == 9


def valid_row(board, y):
    return valid_seq(board[y])


def valid_column(board, x):
    return valid_seq(sudoku.extract_column(board, x))


def valid_block(board, x, y):
    return valid_seq(sudoku.extract_block(board, x, y))


def check_valid_board(board):
    return (all([valid_row(board, num) and valid_column(board, num) for num in range(9)]) and
            all([valid_block(board, x * 3, y * 3) for x in range(3) for y in range(3)]))


def test_create_board():
    eq_(sudoku.create_board(), [[0] * 9] * 9)
    b = sudoku.create_board()
    b[0][1] = 1
    eq_(b, [[0, 1, 0, 0, 0, 0, 0, 0, 0]] + [[0] * 9] * 8)


def test_valid_for_seq_none():
    eq_(sudoku.valid_for_seq([]), range(1, 10))


def test_valid_for_seq_number_single():
    eq_(sudoku.valid_for_seq([1]), range(2, 10))


def test_valid_for_seq_number_some():
    eq_(sudoku.valid_for_seq([1, 5, 7, 9]), [2, 3, 4, 6, 8])


def test_valid_for_seq_number_all():
    eq_(sudoku.valid_for_seq(range(1, 10)), [])


def test_extract_column():
    eq_(sudoku.extract_column([[1] + [0] * 8] * 9, 0), [1] * 9)


def test_extract_block():
    eq_(sudoku.extract_block([[1] + [0] * 8] * 9, 0, 0), [1, 0, 0] * 3)

    eq_(sudoku.extract_block([[0, 1, 0, 0, 0, 0, 0, 0, 0],
                              [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9], 0, 0),
        [0, 1, 0, 0, 0, 0, 0, 0, 0])

    eq_(sudoku.extract_block([[0, 0, 0, 0, 0, 0, 0, 0, 1],
                              [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9], 7, 0),
        [0, 0, 1, 0, 0, 0, 0, 0, 0])


def test_valid_for_row():
    eq_(sudoku.valid_for_row([[0] * 9, [0, 1, 3, 2, 0, 0, 0, 0, 0]] + [[0] * 9] * 7, 1), [4, 5, 6, 7, 8, 9])


def test_generate_board():
    eq_(check_valid_board(sudoku.generate_sudoku()), True)
