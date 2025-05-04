from utils import print_ret

@print_ret
def shiftRows(state):
    # apenas inverte os nibbles da segunda linha
    return [state[0], [state[1][1], state[1][0]]]