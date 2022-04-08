from meta.t3 import *

tests = [
    lambda: (is_winner([
        "X", 'O', "X", 'O', 'X', 'O','X', 'X', 'O'
    ], 'X'), ' X 246 WIN'),
    lambda: (is_winner([
        "X", 'O', "X", 'O', 'X', 'O','O', 'X', 'X'
    ], 'X'), 'X 048 WIN')
]
