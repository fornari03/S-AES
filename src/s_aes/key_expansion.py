from constants import SBOX, ROUND_CONST

def keyExpansion(key):

    # w0 e w1 (1º e 2º bytes da chave original)
    w0 = [key[0], key[1]]
    w1 = [key[2], key[3]]
    
    round = 1
    gw1 = g(w1, round)

    # faz o XOR entre w0 e g(w1) e entre w2 e w1
    w2 = [w0[i] ^ gw1[i] for i in range(2)]
    w3 = [w2[i] ^ w1[i] for i in range(2)]

    round = 2
    gw3 = g(w3, round)

    # faz o XOR entre w2 e g(w3) e entre w4 e w3
    w4 = [w2[i] ^ gw3[i] for i in range(2)]
    w5 = [w4[i] ^ w3[i] for i in range(2)]


    return [[w0, w1], [w2, w3], [w4, w5]]


def g(w, round_number):
    # rotaciona
    w = [w[1], w[0]]

    # aplica S-box
    w = [SBOX[n] for n in w]

    # XOR com a constante de rodada
    for i in range(2):
        w[i] = w[i] ^ ROUND_CONST[round_number-1][i]

    return w
