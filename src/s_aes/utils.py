import base64


def string_to_binary_number(message):
    binary_str = ''.join(format(ord(c), '08b') for c in message)
    return int(binary_str, 2)


def binary_to_nibble_matrix(binary_number):
    # converte um número binário em uma matriz de nibbles
    binary_str = format(binary_number, '08b')
    padding = 8 - len(binary_str) % 8
    binary_str = binary_str.zfill(len(binary_str)+padding)
    nibbles = [int(binary_str[i:i + 4], 2) for i in range(0, len(binary_str), 4)]
    matrix = [[nibbles[0], nibbles[2]], [nibbles[1], nibbles[3]]]
    return matrix


def nibble_matrix_to_binary_string(matrix):
    # converte a matriz de nibbles de volta para uma string binária
    nibbles = [matrix[0][0], matrix[1][0], matrix[0][1], matrix[1][1]]
    return ''.join(format(nibble, '04b') for nibble in nibbles)

def binary_string_to_base64(bin_str):
    # converte a string binária em uma string base64
    n = int(bin_str, 2)
    b64_str = base64.b64encode(n.to_bytes((n.bit_length() + 7) // 8, 'big')).decode()
    return b64_str

def binary_string_to_hex(bin_str, padding=4):
    # converte a string binária em uma string hexadecimal
    n = int(bin_str, 2)
    hex_str = hex(n)[2:].upper()
    return hex_str.zfill(padding)  # preenche com zeros à esquerda (padding)


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