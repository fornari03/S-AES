from utils import string_to_binary_string

message = input()
message = string_to_binary_string(message)

key = 0xABCD # chave de 16 bits
print(key)

# keys = keyExpansion(key)

# addRoundKey(message, keys[0])

# faz as duas rodadas de substituição e permutação

# mostra o resultado em base64
# print(base64.b64encode(result))