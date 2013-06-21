BOARD_SIZE = 9
import copy

def create_board():
    board = []
    for i in range(0, BOARD_SIZE):
        board.append([0] * BOARD_SIZE)

    return board


def print_board(board):
    print '\n'.join(['%s' % row for row in board])


def valid_for_row(row, number_to_check):
    return number_to_check not in row


def valid_for_column(column, number_to_check):
    return number_to_check not in column


def valid_for_block(block, number_to_check):
    return number_to_check not in block


def available_numbers(seq):
    return [num for num in range(1, 10) if num not in seq]


def extract_column(board, index):
    return [row[index] for row in board]


def extract_block(board, blockX, blockY):
    row_offset = blockY * 3
    column_offset = blockX * 3
    block_size = 3
    block = []

    for row_index in range(row_offset, row_offset + block_size):
        block.extend(board[row_index][column_offset:column_offset+block_size])

    return block


def find_block_index(x, y):
    return x / 3, y / 3

def has_next(y, x):
    if x == BOARD_SIZE - 1 and y == BOARD_SIZE - 1:
        return False
    return True

def next(y, x):
    if x < BOARD_SIZE - 1:
        return (y, x + 1)
    elif x == BOARD_SIZE - 1:
        assert(y < BOARD_SIZE)
        return (y + 1, 0)
    else:
        assert(0)


def generate_sudoku():
    board = create_board()
    generate_sudoku_recurse(board, 0, 0)
    return board

NITER = 0
def generate_sudoku_recurse(board, y, x):
    global NITER
    NITER += 1
    print "generate_sudoku_recurse(", y, ", ", x, ")"
    for i in range(1,10):
        if valid_for_block(extract_block(board, x/3, y/3), i)\
            and valid_for_row(board[y], i)\
            and valid_for_column(extract_column(board, x), i):

            newboard = copy.deepcopy(board)
            print "found: ", i, "NITER: ", NITER
            newboard[y][x] = i
            print_board(newboard)
            if has_next(y, x):
                if generate_sudoku_recurse(newboard, *next(y, x)):
                    board = newboard
                    return True
                 
            else:
                board = newboard
                return True
    return False


if __name__ == "__main__":
    #generate_sudoku()
    print_board(generate_sudoku())
