def get_neighbors(cell):
    return set([(cell[0] + deltaX, cell[1] + deltaY)
                    for deltaX in range(-1, 2)
                    for deltaY in range(-1, 2)
                    if deltaX != 0 or deltaY != 0])

def is_alive(cell, board):
    alive_neighbors = set([neighbor for neighbor in get_neighbors(cell)
                                    if neighbor in board])

    return len(alive_neighbors) == 3 or (len(alive_neighbors) == 2 and cell in board)


def next_gen(board):
    candidates = set([candidate for cell in board
                                for candidate in get_neighbors(cell)])

    return set([cell for cell in candidates
                     if is_alive(cell, board)])
