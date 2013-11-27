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


def set_pacman(board, column, row, heading):
    board[row] = (board[row][:column] + get_pacman_char(heading) + board[row][column + 1:])
    return board


def search_pacman(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] in PACMAN_REPRS:
                return (column, row)


if __name__ == "__main__":
    print level_to_string(["...", "...", "...", "...", "..."])
