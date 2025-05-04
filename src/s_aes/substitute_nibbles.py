from constants import SBOX
from utils import print_ret

@print_ret
def substituteNibbles(state):
    # substitui os nibbles da matriz de estado pela S-Box
    return [[SBOX[nibble] for nibble in row] for row in state]
