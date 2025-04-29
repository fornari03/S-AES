from utils import print_ret

@print_ret
def shiftRows(state):
    return [state[0], [state[1][1], state[1][0]]]