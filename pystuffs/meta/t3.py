from functools import reduce
from util import uDecorators as ud

# Type Signatures
Point = tuple[int, int]
Placements = list[int]
Priorities = list[int]
Neighbours = tuple[int]
Neighbours_POINT = tuple[int]
# PURE FUNCTIONS I guess
# GLOBAL: Utility functions
#decorator

diadic = ud.curried(2)
triadic = ud.curried(3)

use = lambda t: lambda f: f(t)

get_2d_frm_1d = diadic(lambda dim, idx: (idx//dim, idx%dim))
get_1d_frm_2d = diadic(lambda dim, p: p[0]*dim + p[1])

incr = lambda n: n + 1
decr = lambda n: n - 1

# use this to append: list inedex item
@triadic
def update(lst: list, idx: int, itm: any) -> list:
    return [*lst[:idx], itm, *lst[idx+1:]]

# list processors
def init_priorities() -> Priorities:
    return  [0 for _ in range(9)]

def init_placements() -> Placements:
    return [None for _ in range(9)]

def get_2d_nbrs(i: Point) -> Neighbours_POINT:
    r, c = i
    return [point for point in [
        (r-1, c-1), (r-1, c), (r-1, c+1),
        (r, c-1), (r, c+1),
        (r+1, c-1), (r+1, c), (r+1, c+1)
    ]]

# binary nodes

@diadic
def is_valid_point(plc: Placements, p: Point) -> bool:
    l = int(len(plc)**0.5)
    r, c = p
    if r < 0 or r >= l: return False
    if c < 0 or c >= l: return False
    return True

@diadic
def is_valid_idx(plc: Placements, idx: int) -> bool:
    if idx<0 or idx>=len(plc): return False
    return True

@diadic
def is_free(plc: Placements, idx: int) -> bool:
    return not plc[idx]

@diadic
def is_valid_selection(plc: Placements, idx: int) -> bool:
    return is_valid_idx(plc, idx) and is_free(plc, idx)

@diadic
def is_winner(plc: Placements, key:str) -> bool:
    return any(map(lambda f: f(plc, key), [
        check_verticals, check_horizontals,
        check_diagonal_left, check_diagonal_right
    ]))

# Win conditions
@diadic
def check_horizontals(plc: Placements, key:str) -> bool:
    l = int(len(plc)**0.5)
    return any(map(
        lambda s: all(key == k for k in plc[s:s+l]), range(0,len(plc), l)
    ))

# vertical = (r-1, c), (r+1, c)
@diadic
def check_verticals(plc: Placements, key: str) -> bool:
    l = int(len(plc)**0.5)
    return any(map(lambda s: all(key == k for k in plc[s::l]), range(l)))

# diagonal_left = (r-1, c-1), (r+1, c+1) : Li*(L+1)
@diadic
def check_diagonal_left(plc: Placements, key: str) -> bool:
    l = int(len(plc)**0.5)
    return all(key == i for i in plc[::l+1])

# diagonal_right  = (r-1, c+1), (r+1, c-1)
@diadic
def check_diagonal_right(plc: Placements, key: str) -> bool:
    l = int(len(plc)**0.5)
    return all(key == i for i in plc[l-1:len(plc)-1:l-1])

#Impure
# IO section
def get_user_input(key: str) -> int:
    x = input(f'Choose Location for >> {key} <<: ')
    return int(x) if x.isdigit() else get_user_input(key)
# IOEND

def handle_selection(
    plc: Placements,
    prt: Priorities,
    sel: int,
    key:str
) -> any:
    if is_valid_selection(plc, sel):
        iPlace = use(plc)

        nplc = update(plc, sel, key.upper())
        nprt = []
        l = len(nplc)**0.5

        validate_cord = lambda p: is_valid_point(l, p)
        get_1d = lambda p: get_1d_frm_2d(l, p)

        cords = get_2d_nbrs(get_2d_frm_1d(l, sel))
        nbrs = map(get_1d, filter(validate_cord, cords))

        for n in nbrs:
            if key == 'O': nprt = update(prt, n, decr(prt[n]))
            else: nprt = update(prt, n, incr(prt[n]))
        return nplc, nprt
    return False

#composites
def actions(plc: Placements) -> filter:
    return filter(lambda idx: is_free(plc, idx), range(len(plc)))

@triadic
def transition(state: Placements, idx: int, key: str) -> Placements:
    return update(state, idx, key.upper())

@diadic
def terminal(plc: Placements, keys: list[str]) -> bool:
    return not any(actions(plc)) or any(is_winner(plc, key) for key in keys)
    #is_winner(plc, 'X') or is_winner(plc, 'O')

def evaluate(plc: Placements) -> int:
    if is_winner(plc, 'X'): return 1
    if is_winner(plc, 'O'): return -1
    return 0

#with_board = use(board)
