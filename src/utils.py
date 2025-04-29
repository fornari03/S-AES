def string_to_binary_string(msg: str) -> str:
    bin_str = ''.join(format(ord(i), '08b') for i in msg)
    if len(bin_str) < 16:
        return bin_str.ljust(16, '0')  # padding com 0s
    elif len(bin_str) > 16:
        return bin_str[:16]  # corta se passar
    return bin_str


def binary_string_to_nibble_matrix(bin_str: str):
    # converte a string binária em uma matriz de nibbles
    nibbles = [int(bin_str[i:i+4], 2) for i in range(0, 16, 4)]
    return [[nibbles[0], nibbles[2]], [nibbles[1], nibbles[3]]]


def print_ret(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Estado após '{func.__name__}':")
        print_matrix(result)
        return result
    return wrapper

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()