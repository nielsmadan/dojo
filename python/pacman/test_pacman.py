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
    new_board = pacman.move_pacman(["..", "<.", ".."])
    eq_(new_board, ["..", " <", ".."])


def test_move_pacman_left():
    new_board = pacman.move_pacman(["..", ".>", ".."])
    eq_(new_board, ["..", "> ", ".."])


def test_move_pacman_up():
    new_board = pacman.move_pacman(["..", ".V", ".."])
    eq_(new_board, [".V", ". ", ".."])


def test_move_pacman_down():
    new_board = pacman.move_pacman(["..", ".A", ".."])
    eq_(new_board, ["..", ". ", ".A"])


def test_change_pacman_heading():
    new_board = pacman.change_pacman_heading(["..", ".A", ".."], pacman.UP)
    eq_(new_board, ["..", ".V", ".."])
