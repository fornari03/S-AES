from utils import print_ret

@print_ret
def mixColumns(state):
    # faz a multiplicação de matriz em GF(2⁴)
    mix_matrix = [[1, 4], [4, 1]] # matriz fixa do S-AES
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            # faz a multiplicação no campo de Galois, elemento a elemento
            result[i][j] = galois_mult(mix_matrix[i][0], state[0][j]) ^ galois_mult(mix_matrix[i][1], state[1][j])
    return result

def galois_mult(a, b):
    # multiplicação no campo de Galois GF(2⁴)
    result = 0

    for i in range(4):
        # se o LSB de 'b' for 1, fazemos XOR do acumulador com 'a'
        if b & 1: 
            result ^= a

        # se o MSB de 'a' (em 4 bits) for 1, vai ter carry
        carry = a & 0b1000

        # multiplica 'a' por 2 e mantém apenas 4 bits
        a = (a << 1) & 0b1111

        if carry:
            a ^= 0b10011 # x⁴ + x + 1

        b >>= 1 # volta o loop e analisa o próximo bit de b

    # pega os 4 LSB
    return result & 0b1111
