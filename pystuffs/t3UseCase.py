from meta import t3

class Key:
    x: str = 'X'
    o: str = 'O'
    all: callable = lambda: [Key.x, Key.o]

##############random
def showBoard(board: t3.Placements) -> None:
    l = int(len(board)**0.5)
    buffer = ''
    for i in range(l):
        for j in range(l):
            k = t3.get_1d_frm_2d(l, (i, j))
            buffer += (str(board[k]) if board[k] else str(k)) + ' '
        buffer += '\n'
    print(buffer)

def gameplay(board, keys, turn=0):
    iBoard = t3.use(board)

    set_Board = lambda action: iBoard(t3.update)(*action)

    showBoard(board)
    if t3.terminal(board, keys):
        return t3.evaluate(board)
    k = turn%2

    ip = t3.get_user_input(keys[k])
    b = board

    if not t3.is_valid_idx(board, ip) or (not t3.is_free(board, ip)):
        return gameplay(board, keys, turn)
    # transition
    action = (ip, keys[k])
    b = set_Board(action)
    ##
    return gameplay(b, keys, turn+1)

print(gameplay(t3.init_placements(), Key.all()))
#print(init_placements()[0])
#print(gameplay(init_placements()))
