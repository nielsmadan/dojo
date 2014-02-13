from nose.tools import eq_

import pacman


def test_1x1_create_level():
    level = pacman.create_level(1, 1)
    eq_(level, ["."])


def test_3x5_create_level():
    level = pacman.create_level(3, 5)
    eq_(level, ["...", "...", "...", "...", "..."])


def test_0x0_create_level():
    level = pacman.create_level(0, 0)
    eq_(level, [])


def test_1x0_create_level():
    level = pacman.create_level(1, 0)
    eq_(level, [])


def test_0x1_create_level():
    level = pacman.create_level(0, 1)
    eq_(level, [])


def test_1x1_level_to_string():
    level_string = pacman.level_to_string(["."])

    eq_(level_string, ".\n")


def test_3x5_level_to_string():
    level_string = pacman.level_to_string(["...", "...", "...", "...", "..."])

    eq_(level_string, "...\n...\n...\n...\n...\n")


def test_set_pacman():
    board = pacman.set_pacman(["...", "...", "...", "...", "..."], 1, 1, pacman.RIGHT)

    eq_(board, ["...", ".<.", "...", "...", "..."])


def test_set_pacman_edge():
    board = pacman.set_pacman(["...", "...", "...", "...", "..."], 0, 0, pacman.RIGHT)

    eq_(board, ["<..", "...", "...", "...", "..."])


def test_set_pacman_corner():
    board = pacman.set_pacman(["...", "...", "...", "...", "..."], 2, 4, pacman.RIGHT)

    eq_(board, ["...", "...", "...", "...", "..<"])


def test_get_pacman_char_looking_left():
    pacman_char = pacman.get_pacman_char(pacman.LEFT)
    eq_(pacman_char, ">")


def test_search_pacman():
    pacman_pos = pacman.search_pacman(["...", "...", "...", "...", "..<"])
    eq_(pacman_pos, (2, 4, '<'))

def test_search_ghost():
    ghost_pos = pacman.search_ghost(["...", "...", "...", "...", "..@"])
    eq_(ghost_pos, (2, 4, '@'))


def test_find_new_pos_right():
    new_board = pacman.find_new_pos(["..", "<.", ".."])
    eq_(new_board, (1, 1))


def test_find_new_pos_left():
    new_board = pacman.find_new_pos(["..", ".>", ".."])
    eq_(new_board, (0, 1))


def test_find_new_pos_up():
    new_board = pacman.find_new_pos(["..", ".V", ".."])
    eq_(new_board, (1, 0))


def test_find_new_pos_down():
    new_board = pacman.find_new_pos(["..", ".A", ".."])
    eq_(new_board, (1, 2))


def test_find_new_pos_right_edge():
    new_board = pacman.find_new_pos(["..",
                                     ".<",
                                     ".."])
    eq_(new_board, (0, 1))


def test_find_new_pos_left_edge():
    new_board = pacman.find_new_pos(["..",
                                     ">.",
                                     ".."])
    eq_(new_board, (1, 1))


def test_find_new_pos_up_edge():
    new_board = pacman.find_new_pos(["V.",
                                     "..",
                                     ".."])
    eq_(new_board, (0, 2))


def test_find_new_pos_down_edge():
    new_board = pacman.find_new_pos(["..",
                                     "..",
                                     "A."])
    eq_(new_board, (0, 0))


def test_clear_pos():
    new_board = pacman.clear_pos(["."], 0, 0)
    eq_(new_board, [' '])


def test_move_pacman_right():
    new_state = pacman.move_pacman(pacman.State(["..", "<.", ".."]))
    eq_(new_state.board, ["..", " <", ".."])


def test_move_pacman_left():
    new_state = pacman.move_pacman(pacman.State(["..", ".>", ".."]))
    eq_(new_state.board, ["..", "> ", ".."])


def test_move_pacman_up():
    new_state = pacman.move_pacman(pacman.State(["..", ".V", ".."]))
    eq_(new_state.board, [".V", ". ", ".."])


def test_move_pacman_down():
    new_state = pacman.move_pacman(pacman.State(["..", ".A", ".."]))
    eq_(new_state.board, ["..", ". ", ".A"])


def test_change_pacman_heading():
    new_board = pacman.change_pacman_heading(["..", ".A", ".."], pacman.UP)
    eq_(new_board, ["..", ".V", ".."])


def test_user_input():
    pacman.add_user_input(pacman.UP)

    eq_(pacman.get_next_input(), pacman.UP)


def test_user_input():
    pacman.add_user_input(pacman.UP)
    pacman.add_user_input(pacman.DOWN)

    eq_(pacman.get_next_input(), pacman.UP)
    eq_(pacman.get_next_input(), pacman.DOWN)


def test_nouser_input():
    eq_(pacman.get_next_input(), None)

    pacman.add_user_input(pacman.UP)
    eq_(pacman.get_next_input(), pacman.UP)
    eq_(pacman.get_next_input(), None)


def test_single_tick():
    board = pacman.State(["..", ".A", ".."])
    new_state = pacman.tick(board)
    eq_(new_state.board, ["..", ". ", ".A"])


def test_process_user_input():
    board = ["..", ".A", ".."]
    pacman.add_user_input(pacman.LEFT)
    new_board = pacman.process_user_input(board)
    eq_(new_board, ["..", ".>", ".."])


def test_single_tick_with_user_input():
    state = pacman.State(["..", ".A", ".."])
    pacman.add_user_input(pacman.LEFT)
    new_state = pacman.tick(state)
    eq_(new_state.board, ["..", "> ", ".."])


def test_double_tick_with_user_input():
    state = pacman.State(["..", ".A", ".."])
    pacman.add_user_input(pacman.LEFT)
    pacman.add_user_input(pacman.RIGHT)
    new_state = pacman.tick(state)
    eq_(new_state.board, ["..", "< ", ".."])


def test_get_score_basic():
    state = pacman.State(["<."])
    new_state = pacman.tick(state)

    eq_(new_state.score, 1)


def test_get_score_2scores():
    state = pacman.State(["<.."])
    new_state = pacman.tick(state)
    new_state = pacman.tick(new_state)

    eq_(new_state.score, 2)


def test_get_score_2score_and_space():
    state = pacman.State(["<. ."])
    new_state = pacman.tick(state)
    new_state = pacman.tick(new_state)

    eq_(new_state.score, 1)

def test_get_score_2score_and_wrap():
    state = pacman.State([".<."])
    new_state = pacman.tick(state)
    new_state = pacman.tick(new_state)

    eq_(new_state.score, 2)


def test_wall():
    state = pacman.State(["<#"])
    new_state = pacman.tick(state)
    eq_(new_state.board, ["<#"])


def test_ghost_movement_right():
    state = pacman.State(["<.", "..", "@.", ".."])
    new_state = pacman.tick(state)
    eq_(new_state.board, [" <", "..", ".@", ".."])


def test_ghost_movement_right_near_edge():
    state = pacman.State(["<.", "..", ".@", ".."])
    new_state = pacman.tick(state)
    eq_(new_state.board, [" <", "..", "@.", ".."])


def test_ghost_movement_right_without_dot():
    state = pacman.State(["<.", "..", "o ", ".."])
    new_state = pacman.tick(state)
    eq_(new_state.board, [" <", "..", " o", ".."])


def test_ghost_movement_right_from_dot_to_no_dot():
    state = pacman.State(["<.", "..", "o.", ".."])
    new_state = pacman.tick(state)
    eq_(new_state.board, [" <", "..", " @", ".."])


def test_ghost_movement_right_near_the_wall():
    state = pacman.State(["<.", "..", "@#", ".."])
    new_state = pacman.tick(state)
    eq_(new_state.board, [" <", "..", "@#", ".."])


def test_ghost_movement_to_pacman():
    state = pacman.State(["..", "..", "@.", ".V"])
    new_state = pacman.tick(state)
    state = pacman.State(["..", "..", ".@", ". "])
    eq_(new_state.status, pacman.LEVEL_FAILED)


def test_level_completed():
    board = ["  ", "  ", "<."]
    new_state = pacman.tick(pacman.State(board))
    eq_(new_state.board, ["  ", "  ", " <"])
    eq_(new_state.status, pacman.LEVEL_COMPLETED)


def test_level_in_progress():
    board = ["  ", "..", "<."]
    new_state = pacman.tick(pacman.State(board))
    eq_(new_state.board, ["  ", "..", " <"])
    eq_(new_state.status, pacman.LEVEL_IN_PROGRESS)


def test_level_end_to_end():
    board = ["<.", ".."]

    new_state = pacman.tick(pacman.State(board))
    eq_(new_state.board, [" <", ".."])
    eq_(new_state.status, pacman.LEVEL_IN_PROGRESS)

    pacman.add_user_input(pacman.DOWN)
    new_state = pacman.tick(new_state)
    eq_(new_state.board, ["  ", ".A"])
    eq_(new_state.status, pacman.LEVEL_IN_PROGRESS)

    pacman.add_user_input(pacman.LEFT)
    new_state = pacman.tick(new_state)
    eq_(new_state.board, ["  ", "> "])
    eq_(new_state.status, pacman.LEVEL_COMPLETED)

def test_encounter_wall():
    state = pacman.State([".#<", "..."])
    new_state = pacman.encounter_wall(state)
    eq_(new_state, state)
