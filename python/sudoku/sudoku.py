BOARD_SIZE = 9


def create_board():
    return [[0] * BOARD_SIZE] * BOARD_SIZE


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


def valid_board(


# def generate_sudoku():
#     board = create_board()
# 
#     return generate_sudoku_recurse(board, 0, 0)
# 
# 
# def generate_sudoku_recurse(board, x, y):
#     pass


if __name__ == "__main__":
    print_board(create_board())
