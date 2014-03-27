from collections import deque
RIGHT = '<'
LEFT = '>'
UP = 'V'
DOWN = 'A'

PACMAN_REPRS = [RIGHT, LEFT, UP, DOWN]
GHOST_REPRS = ["o", "@"]
WALL_REPR = '#'

LEVEL_COMPLETED = 0
LEVEL_IN_PROGRESS = 1
LEVEL_FAILED = 2


class State(object):
    def __init__(self, board, status=LEVEL_IN_PROGRESS, score=0):
        self.board = board
        self.status = status
        self.score = score

    def set_cell(self, column, row, new_cell):
        self.board[row] = (self.board[row][:column] + new_cell + self.board[row][column + 1:])
        return self

    def get_pacman_char(self, heading):
        return heading

    def set_pacman(self, column, row, heading):
        return self.set_cell(column, row, self.get_pacman_char(heading))

    def __eq__(self, other):
        return self.board == other.board and self.status == other.status and self.score == other.score


def create_level(width, height):
    if width == 0:
        return []
    else:
        return ["." * width] * height


def level_to_string(board):
    return "\n".join(board) + "\n"


def search_actors(board, actors_reprs):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] in actors_reprs:
                return (column, row, board[row][column])

def search_pacman(board):
    return search_actors(board, PACMAN_REPRS)

def search_ghost(board):
    return search_actors(board, GHOST_REPRS)

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


def clear_pos(state, column, row):
    return state.set_cell(column, row, ' ').board


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
    WALL_REPR: encounter_wall,
    '@': encounter_ghost
}


def move_pacman(state):
    new_column, new_row = find_new_pos(state.board)
    column, row, heading = search_pacman(state.board)
    board = clear_pos(state, column, row)

    return state.set_pacman(new_column, new_row, heading)

def find_new_ghost_pos(state):
    max_column = len(state.board[0])
    max_row = len(state.board)

    column_pos, row_pos, _ = search_ghost(state.board)

    # always heading right (for now)
    new_column_pos = (column_pos + 1) % max_column

    if state.board[row_pos][new_column_pos] == WALL_REPR:
        return (column_pos, row_pos)
    elif state.board[row_pos][new_column_pos] in PACMAN_REPRS:
        state.status = LEVEL_FAILED
        return (column_pos, row_pos)

    return (new_column_pos, row_pos)

def move_ghost(state):
    ghost = search_ghost(state.board)

    if ghost is None:
        return state

    new_column, new_row = find_new_ghost_pos(state)
    column, row, character = ghost

    new_cell = "."
    if character == "o":
        new_cell = " "

    new_ghost = "@"
    if state.board[new_row][new_column] == " ":
        new_ghost = "o"

    return state.set_cell(column, row, new_cell).set_cell(new_column, new_row, new_ghost)


def change_pacman_heading(state, new_heading):
    column, row, heading = search_pacman(state.board)
    return state.set_pacman(column, row, new_heading).board


user_input_queue = deque()


def add_user_input(key):
    user_input_queue.append(key)


def get_next_input():
    if len(user_input_queue) == 0:
        return None

    return user_input_queue.popleft()

def process_user_input(state):
    next_input = get_next_input()

    while next_input != None:
        state.board = change_pacman_heading(state, next_input)
        next_input = get_next_input()

    return state.board

def handle_pacman(state):
    new_column, new_row = find_new_pos(state.board)
    return ENCOUNTER_MAP[state.board[new_row][new_column]](state)

def handle_ghost(state):
    return move_ghost(state)

def tick(state):
    state.board = process_user_input(state)
    newstate = handle_pacman(state)
    newstate = handle_ghost(newstate)

    return newstate

if __name__ == "__main__":
    print level_to_string(["...", "...", "...", "...", "..."])
