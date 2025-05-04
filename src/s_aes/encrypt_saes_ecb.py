from encrypt_saes import encrypt_saes
from utils import binary_string_to_hex, binary_string_to_base64


def encrypt_saes_ecb(message, key):
    # divide em blocos de dois caracteres (16 bits)
    blocks = [message[i:i+2] for i in range(0, len(message), 2)]

    # faz padding PKCS#7 no LSB se for menor que 16 bits
    if len(blocks[-1]) < 2:
        blocks[-1] += '#' # # para mostrar que é padding (seria util na decriptacao)

    encrypted_binary = ""
    for block in blocks:
        ciphertext_block = encrypt_saes(block, key)
        encrypted_binary += ciphertext_block

    print("-" * 50)
    print("\nTexto encriptado com S-AES em ECB:")

    # print(f"Texto cifrado em binário: {encrypted_binary}")
    
    print(f"Texto cifrado em hexadecimal: 0x{binary_string_to_hex(encrypted_binary, len(blocks) * 4)}")


    return binary_string_to_base64(encrypted_binary)


# testando o ECB
message = input("Digite a mensagem a ser cifrada: ")

key = input("Digite a chave em hexadecimal (e.g.: 0xA73B): ")
key = ["0x"+key[i] for i in range(2, len(key))]
key = [int(k, 16) for k in key]

cipher_text = encrypt_saes_ecb(message, key)
print(f"Texto cifrado em base64: {cipher_text}")