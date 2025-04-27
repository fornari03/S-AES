from utils import string_to_binary_string, binary_string_to_nibble_matrix
from key_expansion import keyExpansion

message = input()
message = string_to_binary_string(message)
message = binary_string_to_nibble_matrix(message)

key = [0xA, 0xB, 0xC, 0xD] # chave de 16 bits em 4 nibbles

keys = keyExpansion(key)

# addRoundKey(message, keys[0])

# faz as duas rodadas de substituição e permutação

# mostra o resultado em base64
# print(base64.b64encode(result))