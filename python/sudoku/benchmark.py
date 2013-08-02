import timeit


if __name__ == "__main__":
    print timeit.timeit("solve_sudoku.solve_hard_puzzle", setup="import solve_sudoku", number=100000000)
