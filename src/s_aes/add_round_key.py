from utils import print_ret

@print_ret
def addRoundKey(state, nibble_matrix_key):
    # primeiro ajusta a matriz de nibbles da chave
    nibble_matrix_key[0][1], nibble_matrix_key[1][0] = nibble_matrix_key[1][0], nibble_matrix_key[0][1]
    for i in range(2):
        for j in range(2):
            state[i][j] = state[i][j] ^ nibble_matrix_key[i][j] # faz o XOR
    return state