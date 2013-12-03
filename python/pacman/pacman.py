RIGHT = '<'
LEFT = '>'
UP = 'V'
DOWN = 'A'

PACMAN_REPRS = [RIGHT, LEFT, UP, DOWN]


def get_pacman_char(heading):
    return heading


def create_level(width, height):
    if width == 0:
        return []
    else:
        return ["." * width] * height


def level_to_string(board):
    return "\n".join(board) + "\n"


def set_cell(board, column, row, new_cell):
    board[row] = (board[row][:column] + new_cell + board[row][column + 1:])
    return board


def set_pacman(board, column, row, heading):
    return set_cell(board, column, row, get_pacman_char(heading))


def search_pacman(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] in PACMAN_REPRS:
                return (column, row, board[row][column])


def find_new_pos(board):
    max_column = len(board[0])
    max_row = len(board)

    column_pos, row_pos, heading = search_pacman(board)
    new_column_pos = column_pos
    new_row_pos = row_pos

    if heading == RIGHT:
        new_column_pos = (column_pos + 1) % max_column
    elif heading == LEFT:
        new_column_pos = (column_pos - 1) % max_column
    elif heading == UP:
        new_row_pos = (row_pos - 1) % max_row
    elif heading == DOWN:
        new_row_pos = (row_pos + 1) % max_row

    return (new_column_pos, new_row_pos)


def clear_pos(board, column, row):
    return set_cell(board, column, row, ' ')


def move_pacman(board):
    column, row, heading = search_pacman(board)
    new_column, new_row = find_new_pos(board)
    board = clear_pos(board, column, row)
    board = set_pacman(board, new_column, new_row, heading)
    return board


def change_pacman_heading(board, new_heading):
    column, row, heading = search_pacman(board)
    return set_pacman(board, column, row, new_heading)


if __name__ == "__main__":
    print level_to_string(["...", "...", "...", "...", "..."])
