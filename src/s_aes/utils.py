import base64


def string_to_binary_string(msg):
    bin_str = ''.join(format(ord(i), '08b') for i in msg)
    if len(bin_str) < 16:
        return bin_str.ljust(16, '0')  # padding com 0s
    elif len(bin_str) > 16:
        return bin_str[:16]  # corta se passar
    return bin_str


def binary_string_to_nibble_matrix(bin_str):
    # converte a string binária em uma matriz de nibbles
    nibbles = [int(bin_str[i:i+4], 2) for i in range(0, 16, 4)]
    return [[nibbles[0], nibbles[2]], [nibbles[1], nibbles[3]]]


def nibble_matrix_to_binary_string(matrix):
    # converte a matriz de nibbles de volta para uma string binária
    nibbles = [matrix[0][0], matrix[1][0], matrix[0][1], matrix[1][1]]
    return ''.join(format(nibble, '04b') for nibble in nibbles)

def binary_string_to_base64(bin_str):
    # converte a string binária em uma string base64
    n = int(bin_str, 2)
    b64_str = base64.b64encode(n.to_bytes((n.bit_length() + 7) // 8, 'big')).decode()
    return b64_str

def binary_string_to_hex(bin_str):
    # converte a string binária em uma string hexadecimal
    n = int(bin_str, 2)
    hex_str = hex(n)[2:].upper()
    return hex_str.zfill(4)  # preenche com zeros à esquerda para garantir 4 dígitos


def print_ret(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Estado após '{func.__name__}':")
        print_matrix(result)
        return result
    return wrapper

def print_matrix(matrix):
    for row in matrix:
        row = [int_to_hex(num) for num in row]
        print(f"{'  '.join(row)}")
    print("-" * 50)

def int_to_hex(n):
    # converte um inteiro em uma string hexadecimal
    return hex(n)[2:].upper()