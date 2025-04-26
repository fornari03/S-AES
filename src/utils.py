def string_to_binary_string(msg: str) -> str:
    bin_str = ''.join(format(ord(i), '08b') for i in msg)
    if len(bin_str) < 16:
        return bin_str.ljust(16, '0')  # padding com 0s
    elif len(bin_str) > 16:
        return bin_str[:16]  # corta se passar
    return bin_str