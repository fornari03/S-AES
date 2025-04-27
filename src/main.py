from utils import string_to_binary_string, binary_string_to_nibble_matrix
from key_expansion import keyExpansion
from add_round_key import addRoundKey
from substitute_nibbles import substituteNibbles

message = input()
message = string_to_binary_string(message)
message = binary_string_to_nibble_matrix(message)

key = [0xA, 0xB, 0xC, 0xD] # chave de 16 bits em 4 nibbles

nibble_keys = keyExpansion(key)

state = addRoundKey(message, nibble_keys[0:2]) # w0 e w1

# primeira rodada:
state = substituteNibbles(state)
# state = shiftRows(state)
# state = mixColumns(state)
state = addRoundKey(state, nibble_keys[2:4]) # w2 e w3

# segunda rodada:

# mostra o resultado em base64
# print(base64.b64encode(result))