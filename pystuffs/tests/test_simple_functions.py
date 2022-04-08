from meta.t3 import *

tests = [
    lambda: (init_priorities() == [0,0,0,0,0,0,0,0,0], "Sample Data Test"),
    lambda: (init_placements() == [
        None, None, None, None, None, None, None, None, None
    ], "Sample Data Test"),
    lambda: (get_2d_frm_1d(3, 2) == (0,2), "2d of 2 should be (0,2) :lim = 3"),
    lambda: (get_1d_frm_2d(3, (0,2)) == 2, "1d of (0,2) should be 2 :lim = 3"),
    lambda: (not is_valid_idx([0,0], 4),"should be invalid 2d idx"),
    lambda: (is_free([None, 'x'], 0), 'Should be True there is free space'),
    lambda: (not is_free([None, 'x'], 1), 'Shouldn\'t be True there is no free space'),
    lambda: (update([None, 'x'], 0, 'O') == ['O', 'x'], 'expected [O, x]'),
    lambda: (update([0, 0], 1, incr(0)) == [0, 1], 'expected [0, 1]'),
    lambda: (update([2, 1], 0, decr(2)) == [1, 1], 'expected [1, 1]'),
    lambda: (is_valid_selection([None, 'X'], 0), 'Location should be available'),
    lambda: (not is_valid_selection([None, 'X'], 1), 'Location shouldn\'t be available'),
    lambda: (get_2d_nbrs((1,1)) == [
        (0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2,2)
    ], 'Should get All 8 Neighbours'),
    lambda: (not check_horizontals(init_placements(), "X"), 'no horizontal Xany'),
    lambda: (not check_horizontals([0, 1, "X", 'X'], 'o'), 'no horizontal o23'),
    lambda: (check_horizontals([0, 1, "X", 'X'], 'X'), 'horizontal X23'),
    lambda: (not check_horizontals([0, 1, "X", 'X'], 'x'), 'no horizontal x23'),
    lambda: (check_verticals(["X", 1, "X", 'X'], 'X'), 'vertical X02'),
    lambda: (check_verticals([
        "X", 'O', "X", 'O', 'O', 'X','O', 'X', 'X'
    ], 'X'), 'vertical X258'),
    lambda: (check_diagonal_left([
        "X", 'O', "X", 'O', 'X', 'O','O', 'X', 'X'
    ], 'X'), 'diagonal X048'),
    lambda: (check_diagonal_right([
        "X", 'O', "X", 'O', 'X', 'O','X', 'X', 'O'
    ], 'X'), 'diagonal X 246')
]
