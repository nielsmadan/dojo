import sudoku
import copy


def find_solutions(board):
    pass


def find_solution(board):
    for x in range(9):
        for y in range(9):
            if board[y][x] == 0:
                valid_nums = sudoku.valid_numbers(board, y, x)
                if len(valid_nums) == 1:
                    new_board = copy.deepcopy(board)
                    new_board[y][x] = valid_nums[0]
                    return find_solution(new_board)

    if all([board[y][x] != 0 for y in range(9) for x in range(9)]):
        return board


if __name__ == "__main__":
    board = sudoku.generate_sudoku()
    solved_board = copy.deepcopy(board)

    for num in range(9):
        board[num][0] = 0

    result = find_solution(board)
    sudoku.print_board(result)
    assert result == solved_board
