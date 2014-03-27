// (0, 0), (1, 0)

//fn get_neighbors(cell: (int, int)) -> [(int, int), .. 8] {
//    return [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)];
//}


fn get_neighbors(cell: (int, int)) -> ~[(int, int)] {
    let (m, n) = cell;
    let mut ret: ~[(int, int)] = ~[];
    for x in range(-1, 2) {
        for y in range(-1, 2) {
            if (x != 0 || y != 0) {
                ret.push((m + x, n + y))
            }
        }
    }

    return ret
}

fn get_alive_neighbors(cell: (int, int), board: ~[(int, int)]) -> int {
    let n = get_neighbors(cell);

    let mut ret = 0;
    for x in n.iter() {
        if (board.contains(x)) {
            ret += 1;
        }
    }

    return ret;
}

fn is_alive(cell: (int, int), board: ~[(int, int)]) -> bool {
    let n = get_alive_neighbors(cell, board);

    return n >= 2 && n <= 3
}

fn find_candidate_cells(cells: ~[(int, int)]) -> ~[(int, int)] {
    let cell: (int, int) = cells[0];
    return get_neighbors(cell);
}

#[test]
fn test_get_neighbors() {
    assert_eq!(get_neighbors((0, 0)), ~[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]);
    assert_eq!(get_neighbors((1, 1)), ~[(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]);
}

#[test]
fn test_find_candidate_cells() {
    assert_eq!(find_candidate_cells(~[(0, 0)]), ~[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]);
    assert_eq!(find_candidate_cells(~[(0, 0), (1, 1)]),
                    ~[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1),
                      (0, 0), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]);
}

#[test]
fn test_get_alive_neighbors() {
    assert_eq!(get_alive_neighbors((0, 0), ~[(0, 0), (1, 1)]), 1);
    assert_eq!(get_alive_neighbors((0, 0), ~[(0, 0), (1, 1), (-1, -1)]), 2);
}

#[test]
fn test_is_alive() {
    assert_eq!(is_alive((0, 0), ~[(0, 0), (1, 1)]), false);
    assert_eq!(is_alive((0, 0), ~[(0, 0), (1, 1), (-1, -1)]), true);
    assert_eq!(is_alive((0, 0), ~[(0, 0), (-1, 0), (1, 0), (1, 1), (-1, -1)]), false);
}
