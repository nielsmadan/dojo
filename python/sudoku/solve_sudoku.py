import sudoku
import copy


GLOBAL_COUNTER = 0


def count_calls(fn):
    def __inner(*args, **kwargs):
        global GLOBAL_COUNTER
        GLOBAL_COUNTER += 1
        return fn(*args, **kwargs)

    return __inner


def board_completed(board):
    return all([board[y][x] != 0 for y in range(9) for x in range(9)])


# def foo():
#     list = []
#     for entry in board:
#         if board[entry] == 0:
#             list.push(entry)
#     sort(list, valid_combination_count)
#
#     for i in range(list):
#         list.remove(i)
#         # find the valid solutions for i position
#         if count > 0:


# @count_calls
def find_solution(board):
    if board_completed(board):
        return board
    else:
        y, x = sudoku.next_xy(board)

        valid_nums = sudoku.valid_for_cell(board, y, x)
        for num in valid_nums:
            newboard = copy.deepcopy(board)
            newboard[y][x] = num

            nxt = find_solution(newboard)
            if nxt is not None:
                return nxt


def solve_hard_puzzle():
    board = [
             [4, 0, 0, 0, 0, 0, 0, 0, 2],
             [1, 0, 7, 0, 0, 2, 5, 0, 0],
             [6, 0, 0, 5, 0, 0, 0, 8, 0],
             [0, 0, 0, 0, 9, 4, 6, 7, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 3, 6, 8, 7, 0, 0, 0, 0],
             [0, 8, 0, 0, 0, 7, 0, 0, 5],
             [0, 0, 1, 9, 0, 0, 3, 0, 6],
             [2, 0, 0, 0, 0, 0, 0, 0, 7],
             ]

    return find_solution(board)

if __name__ == "__main__":
    sudoku.print_board(solve_hard_puzzle())
