from utils import string_to_binary_number, binary_to_nibble_matrix, nibble_matrix_to_binary_string, binary_string_to_base64, binary_string_to_hex, int_to_hex
from key_expansion import keyExpansion
from add_round_key import addRoundKey
from substitute_nibbles import substituteNibbles
from shift_rows import shiftRows
from mix_columns import mixColumns


def encrypt_saes(message, key):

    message = string_to_binary_number(message)

    print("-" * 50)
    print(f"Mensagem original em binário: {bin(message)}")

    in_matrix = binary_to_nibble_matrix(message)

    # mostra a matriz de entrada
    print("-" * 50)
    print("Matriz de entrada:")
    for row in in_matrix:
        row = [int_to_hex(num) for num in row]
        print(f"{'  '.join(row)}")
    print("-" * 50)


    round_keys = keyExpansion(key) # retorna as 3 subchaves em matrizes 2x2 de nibbles

    # mostra as chaves expandidas
    print(f"Chave expandidas:")
    for i in range(len(round_keys)):
        print(f"w{i}: {round_keys[i]}")
    print("-" * 50)



    state = addRoundKey(in_matrix, round_keys[0]) # w0 e w1

    # PRIMEIRA RODADA:
    print("Primeira rodada:")
    
    state = substituteNibbles(state)

    state = shiftRows(state)

    state = mixColumns(state)

    state = addRoundKey(state, round_keys[1]) # w2 e w3



    # SEGUNDA RODADA:
    print("Segunda rodada:")

    state = substituteNibbles(state)

    state = shiftRows(state)

    out_matrix = addRoundKey(state, round_keys[2]) # w4 e w5


    # mostra a matriz de saída
    print("Matriz de saída:")
    for row in out_matrix:
        row = [int_to_hex(num) for num in row]
        print(f"{'  '.join(row)}")
    print("-" * 50)


    # converte e mostra a saída em binário, hexadecimal e base64
    cipher_text = nibble_matrix_to_binary_string(out_matrix)
    cipher_text_spaced = ' '.join(cipher_text[i:i+4] for i in range(0, len(cipher_text), 4))
    print(f"Texto cifrado em binário: {cipher_text_spaced}")

    cipher_text_hex = binary_string_to_hex(cipher_text)
    print(f"Texto cifrado em hexadecimal: 0x{cipher_text_hex}")

    cipher_text_64 = binary_string_to_base64(cipher_text)
    print(f"Texto cifrado em base64: {cipher_text_64}")

    return cipher_text