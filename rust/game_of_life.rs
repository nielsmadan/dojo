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

fn will_be_alive(cell: (int, int), board: ~[(int, int)]) -> bool {
    let b = board.contains(&cell);

    let n = get_alive_neighbors(cell, board);

    return (n == 3) || ((n == 2) && b);
}

fn find_candidate_cells(cells: ~[(int, int)]) -> ~[(int, int)] {
    let mut ret: ~[(int, int)] = ~[];

    for cell in cells.iter() {
        let n = get_neighbors(*cell);

        for x in n.iter() {
            if (!ret.contains(x)) {
                ret.push(*x);
            }
        }
    }

    return ret;
}

//fn filtered<T>(lst: ~[T], predicate: |&T| -> bool) -> ~[T] {
//    let mut ret: ~[T] = ~[];
//
//    for elem in lst.iter() {
//        if (predicate(elem)) {
//            let el = elem.clone();
//            ret.push(*el);
//        }
//    }
//
//    return ret;
//}
//
//fn from_iter<T>(it: ~Iterator<T>) -> ~[T] {
//    let mut ret = ~[];
//
//    let n: Option<T> = it.next();
//
//    while (n.is_some()) {
//        ret.push(n.unwrap());
//        n = it.next();
//    }
//
//    return ret;
//}

fn next_gen(cells: ~[(int, int)]) -> ~[(int, int)] {
    let mut ret: ~[(int, int)] = ~[];

    let candidates = find_candidate_cells(cells.clone());

    //return filtered(candidates, |&x| will_be_alive(x, cells.clone()));
    // let mut it = a.iter().map(|&x| 2 * x);
    //return from_iter(candidates.iter().filter(|&x| will_be_alive(*x, cells.clone())));

    for cell in candidates.iter() {
        if (will_be_alive(*cell, cells.clone())) {
            ret.push(*cell);
        }
    }

    return ret;
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
fn test_wll_be_alive() {
    assert_eq!(will_be_alive((0, 0), ~[(0, 0), (1, 1)]), false);
    assert_eq!(will_be_alive((0, 0), ~[(1, 1), (-1, -1)]), false);
    assert_eq!(will_be_alive((0, 0), ~[(-1, 1), (1, 1), (-1, -1)]), true);
    assert_eq!(will_be_alive((0, 0), ~[(0, 0), (1, 1), (-1, -1)]), true);
    assert_eq!(will_be_alive((0, 0), ~[(0, 0), (-1, 0), (1, 0), (1, 1), (-1, -1)]), false);
}

#[test]
fn test_next_gen() {
    assert_eq!(next_gen(~[(0, 0)]), ~[]);
    assert_eq!(next_gen(~[(0, 0), (0, 1), (1, 0), (1, 1)]), ~[(0, 1), (1, 0), (1, 1), (0, 0)]);
    assert_eq!(next_gen(~[(1, 0), (1, 1), (1, 2)]), ~[(0, 1), (1, 1), (2, 1)]);
}

//.x.
//.x.
//.x.
//
//...
//xxx
//...



