from meta.t3 import *

class Boards:
    S00 =  [None for _ in range(9)]
    X246 = [
        "X", 'O', "X",
        'O', 'X', 'O',
        'X', 'X', 'O'
    ]
    X048 = [
        "X", 'O', "X",
        None, 'X', 'O',
        None, 'X', 'X'
    ]
    NTRM2 = [
        'X', 'O',
        None,
        'O', 'X'
    ]
    NTRM12 = [
        "X", None ,
        None,
        'O', 'X'
    ]
    TRM2 = [
        "X", 'O',
        'O', 'X'
    ]
    TRM1 = [
        "X", 'O', "X",
        'O', 'X', 'O',
        'O', 'O', 'X'
    ]
    NTRM22 = ["X", 'O', None]
    DRW = [
        "O", 'O', "X",
        'X', 'X', 'O',
        'O', 'O', 'X'
    ]
    NTRM8 = [
        "O", 'O', "X",
        'X', 'X', 'O',
        'O', 'O', None
    ]
    O147 = [
        "X", 'O', "X",
        'X', 'O', 'O',
        'O', 'O', 'X'
    ]
    NTRM38 = [
        'X', 'O', 'X',
        None, 'O', 'O',
        'X', 'X', None
    ]

TEST_BOARDS: dict[str, list[int]] = {
    'S00': [None for _ in range(9)],
    "X246": [
        "X", 'O', "X",
        'O', 'X', 'O',
        'X', 'X', 'O'
    ],
    'X048': [
        "X", 'O', "X",
        None, 'X', 'O',
        None, 'X', 'X'
    ],
    'NTRM2': [
        "X", 'O',
        None,
        'O', 'X'
    ],
    'NTRM12': [
        "X", None ,
        None,
        'O', 'X'
    ],
    'TRM2': [
        "X", 'O',
        'O', 'X'
    ],
    'TRM1': [
        "X", 'O', "X",
        'O', 'X', 'O',
        'O', 'O', 'X'
    ],
    '2NTRM2': ["X", 'O', None],
    'DRW': [
        "O", 'O', "X",
        'X', 'X', 'O',
        'O', 'O', 'X'
    ],
    'NTRM8': [
        "O", 'O', "X",
        'X', 'X', 'O',
        'O', 'O', None
    ],
    'O147': [
        "X", 'O', "X",
        'X', 'O', 'O',
        'O', 'O', 'X'
    ]
}

class Key:
    x: str = 'X'
    o: str = 'O'

    def as_list(): return [Key.x, Key.o]

get_board = lambda name: use(TEST_BOARDS[name])

iX246 = use(Boards.X246)
iX048 = use(Boards.X048)
iO147 = use(Boards.O147)
iDRW = use(Boards.DRW)
iTRM1 = use(Boards.TRM1)
iTRM2 = use(Boards.TRM2)
iNTRM2 = use(Boards.NTRM2)
iNTRM8 = use(Boards.NTRM8)
iNTRM12 = use(Boards.NTRM12)
iNTRM22 = use(Boards.NTRM22)
iNTRM38 = use(Boards.NTRM38)

B = lambda f: lambda g: lambda a: f(g(a))

tests = [
    lambda: (iX048(is_winner)(Key.x), 'X SHOULD WIN'),
    lambda: (iX246(is_winner)("X"), 'X SHOULD WIN2'),
    lambda: (B(list)(iNTRM2)(actions) == [2], 'NUL 2'),
    lambda: (list(iNTRM12(actions)) == [1, 2], 'NUL 1 2'),
    lambda: (not any(iTRM2(actions)), 'TERMINAL 2'),
    lambda: (iX246(terminal)(Key.as_list()), 'TERMINAL X246'),
    lambda: (iX048(terminal)(Key.as_list()), 'TERMINAL X048'),
    lambda: (iTRM1(terminal)(Key.as_list()), 'TERMINAL 1'),
    lambda: (not iNTRM8(terminal)(Key.as_list()), 'NUL 8'),
    lambda: (iDRW(evaluate) == 0, 'VALUE 0'),
    lambda: (iX048(evaluate) == 1 , 'VALUE 1'),
    lambda: (iO147(evaluate) == -1, 'VALUE 1'),
    lambda: (iNTRM22(transition)(2, 'o') == ['X', 'O', 'O'],'o: UPPER -> PLACE'),
    lambda: (use(iNTRM8(transition)(8)(Key.x))(terminal)(Key.as_list()), 'TERMINAL 3'),
    lambda: (not iDRW(is_winner)('X') and (not iDRW(is_winner)('O')), 'Draw'),
    #lambda: (not iNTRM38(terminal)(Key.as_list()), 'NUL 3 8')
]

#print(iNTRM38(terminal)(Key.as_list()))
