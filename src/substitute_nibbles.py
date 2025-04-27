from constants import SBOX

def substituteNibbles(state):
    return [[SBOX[n] for n in row] for row in state]
