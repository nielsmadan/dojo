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
    eq_(pacman_pos, (2, 4))


# def test_move_pacman():
#     new_board = pacman.move_pacman(["..", "<.", ".."])
