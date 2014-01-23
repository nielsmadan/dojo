from collections import deque
RIGHT = '<'
LEFT = '>'
UP = 'V'
DOWN = 'A'

PACMAN_REPRS = [RIGHT, LEFT, UP, DOWN]

LEVEL_COMPLETED = 0
LEVEL_IN_PROGRESS = 1
LEVEL_FAILED = 2


class State(object):
    def __init__(self, board, status=LEVEL_IN_PROGRESS, score=0):
        self.board = board
        self.status = status
        self.score = score

    def __eq__(self, other):
        return self.board == other.board and self.status == other.status and self.score == other.score


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


def encounter_wall(state):
    return state


def encounter_ghost(state):
    state.status = LEVEL_FAILED
    return state


def encounter_dot(state):
    state.score = state.score + 1

    state = move_pacman(state)

    dot_found = any([cell == "." for row in state.board for cell in row])

    state.status = LEVEL_IN_PROGRESS if dot_found else LEVEL_COMPLETED

    return state


def encounter_space(state):
    return move_pacman(state)


ENCOUNTER_MAP = {
    ' ': encounter_space,
    '.': encounter_dot,
    '#': encounter_wall,
    '@': encounter_ghost
}


def move_pacman(state):
    new_column, new_row = find_new_pos(state.board)
    column, row, heading = search_pacman(state.board)
    board = clear_pos(state.board, column, row)

    board = set_pacman(board, new_column, new_row, heading)

    return State(board, state.status, state.score)


def change_pacman_heading(board, new_heading):
    column, row, heading = search_pacman(board)
    return set_pacman(board, column, row, new_heading)


user_input_queue = deque()


def add_user_input(key):
    user_input_queue.append(key)


def get_next_input():
    if len(user_input_queue) == 0:
        return None

    return user_input_queue.popleft()

def process_user_input(board):
    next_input = get_next_input()

    while next_input != None:
        board = change_pacman_heading(board, next_input)
        next_input = get_next_input()

    return board


def tick(state):
    state.board = process_user_input(state.board)
    new_column, new_row = find_new_pos(state.board)
    newstate = ENCOUNTER_MAP[state.board[new_row][new_column]](state)

    return newstate

if __name__ == "__main__":
    print level_to_string(["...", "...", "...", "...", "..."])
