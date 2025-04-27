def addRoundKey(state, nibble_matrix_key):
    for i in range(2):
        for j in range(2):
            state[i][j] = state[i][j] ^ nibble_matrix_key[i][j]
    return state