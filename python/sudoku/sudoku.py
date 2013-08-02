import random
import copy


BOARD_SIZE = 9
BOARD_MAX_INDEX = BOARD_SIZE - 1


def limit_calls(limit, limit_return=None):
    count = [0]

    def _inner_decorator(fn):
        def _inner_function(*args, **kwargs):
            if count[0] < limit:
                count[0] += 1
                return fn(*args, **kwargs)
            else:
                return limit_return

        return _inner_function

    return _inner_decorator


def create_board():
    board = []
    for i in range(0, BOARD_SIZE):
        board.append([0] * BOARD_SIZE)

    return board


def print_board(board):
    print '\n'.join(['%s' % row for row in board])


def valid_for_seq(seq):
    return [num for num in range(1, 10) if num not in seq]


def valid_for_block(board, x, y):
    return valid_for_seq(extract_block(board, x, y))


def valid_for_column(board, x):
    return valid_for_seq(extract_column(board, x))


def valid_for_row(board, y):
    return valid_for_seq(board[y])


def extract_column(board, index):
    return [row[index] for row in board]


def extract_block(board, blockX, blockY):
    row_offset = blockY - blockY % 3
    column_offset = blockX - blockX % 3
    block_size = 3
    block = []

    for row_index in range(row_offset, row_offset + block_size):
        block.extend(board[row_index][column_offset:column_offset + block_size])

    return block


def generate_sudoku():
    return generate_sudoku_recurse(create_board())


def valid_for_cell(board, y, x):
    return (set(valid_for_block(board, x, y)) &
            set(valid_for_column(board, x)) &
            set(valid_for_row(board, y)))


def next_xy(board):
    return next((y, x) for y in xrange(BOARD_SIZE)
                       for x in xrange(BOARD_SIZE) if board[y][x] == 0)


def board_completed(board):
    return board[BOARD_MAX_INDEX][BOARD_MAX_INDEX] != 0


# @limit_calls(5, True)
def generate_sudoku_recurse(board):
    if board_completed(board):
        return board
    else:
        y, x = next_xy(board)

        valid_nums = list(valid_for_cell(board, y, x))
        random.shuffle(valid_nums)
        for num in valid_nums:
            newboard = copy.deepcopy(board)
            newboard[y][x] = num

            nxt = generate_sudoku_recurse(newboard)
            if nxt is not None:
                return nxt


if __name__ == "__main__":
    print_board(generate_sudoku())
