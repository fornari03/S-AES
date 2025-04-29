from utils import string_to_binary_string, binary_string_to_nibble_matrix, nibble_matrix_to_binary_string, binary_string_to_base64, binary_string_to_hex
from key_expansion import keyExpansion
from add_round_key import addRoundKey
from substitute_nibbles import substituteNibbles
from shift_rows import shiftRows
from mix_columns import mixColumns


message = input()
message = string_to_binary_string(message)
in_matrix = binary_string_to_nibble_matrix(message)
print(f"Início: {in_matrix}")

# key = [0x7, 0x1, 0x4, 0x9] # chave de 16 bits em 4 nibbles
key = [0xA, 0x7, 0x3, 0xB] # chave de 16 bits em 4 nibbles

# in_matrix = [[3,1],[15, 11]]
round_keys = keyExpansion(key)
print(f"Chave expandidas:")
for i in range(len(round_keys)):
    print(f"w{i}: {round_keys[i]}")
print()

state = addRoundKey(in_matrix, round_keys[0:2]) # w0 e w1

# primeira rodada:
state = substituteNibbles(state)

state = shiftRows(state)

state = mixColumns(state)

state = addRoundKey(state, round_keys[2:4]) # w2 e w3

# segunda rodada:
state = substituteNibbles(state)

state = shiftRows(state)

out_matrix = addRoundKey(state, round_keys[4:6]) # w4 e w5


print("Matriz de saída:")
for row in out_matrix:
    print(row)

cipher_text = nibble_matrix_to_binary_string(out_matrix)
cipher_text_spaced = ' '.join(cipher_text[i:i+4] for i in range(0, len(cipher_text), 4))
print(f"Texto cifrado em binário: {cipher_text_spaced}")

cipher_text_hex = binary_string_to_hex(cipher_text)
print(f"Texto cifrado em hexadecimal: 0x{cipher_text_hex}")

cipher_text = binary_string_to_base64(cipher_text)
print(f"Texto cifrado em base64: {cipher_text}")