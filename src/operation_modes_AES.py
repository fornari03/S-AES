from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as crypto_padding
from cryptography.hazmat.primitives.ciphers.modes import CFB, CTR, OFB, CBC, ECB
import base64
import os
import time


def padding(text):
    # padding PKCS#7
    padding_len = 16 - (len(text) % 16) # se len(text) % 16 == 0, add 16 bytes
    return text + bytes([padding_len]) * padding_len # esses bytes são o valor do padding_len

def aes_encrypt(message, key, mode):
    backend = default_backend() # cria o backend para o AES

    if mode == 'ECB':
        start = time.time() # inicia o tempo de execução
        cipher = Cipher(algorithms.AES(key), ECB(), backend=backend) # cria o objeto Cipher com a chave, o modo e o backend
        encryptor = cipher.encryptor() # cria o objeto de encriptação
        cipher_text = encryptor.update(padding(message)) + encryptor.finalize() # cifra a mensagem com padding
        b64_cipher_text = base64.b64encode(cipher_text).decode() # converte o texto cifrado para base64

    elif mode == 'CBC':
        start = time.time()
        init_vector = os.urandom(16) # vetor de inicialização com 16 bytes
        cipher = Cipher(algorithms.AES(key), CBC(init_vector), backend=backend) # cria o objeto Cipher com a chave, o modo e o vetor de inicialização
        encryptor = cipher.encryptor() # cria o objeto de encriptação
        cipher_text = encryptor.update(padding(message)) + encryptor.finalize()
        b64_cipher_text = base64.b64encode(init_vector + cipher_text).decode() # concatena o vetor de inicialização com o texto cifrado

    elif mode == 'CFB':
        start = time.time()
        init_vector = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), CFB(init_vector), backend=backend)
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(message) + encryptor.finalize()
        b64_cipher_text = base64.b64encode(init_vector + cipher_text).decode() # concatena o vetor de inicialização com o texto cifrado

    elif mode == 'OFB':
        start = time.time()
        nonce = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), OFB(nonce), backend=backend)
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(message) + encryptor.finalize()
        b64_cipher_text = base64.b64encode(nonce + cipher_text).decode() # concatena o vetor de inicialização (nonce) com o texto cifrado

    elif mode == 'CTR':
        start = time.time()
        nonce = os.urandom(8)
        # cryptography espera um valor inicial de 16 bytes para o modo CTR
        initial_value = int.from_bytes(nonce + b'\x00' * 8, byteorder='big')
        cipher = Cipher(algorithms.AES(key), CTR(initial_value.to_bytes(16, 'big')), backend=backend)
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(message) + encryptor.finalize()
        b64_cipher_text = base64.b64encode(nonce + cipher_text).decode() # concatena o nonce com o texto cifrado

    end = time.time() # termina o tempo de execução

    print(f"Modo de operação: {mode}")

    print(f"Tempo de execução: {(end - start):.6f} segundos\n")
    
    print(f"Texto cifrado em hexadecimal:")
    
    for i in range(len(cipher_text)//16):
        print("\t" + cipher_text[i*16:(i+1)*16].hex())
    
    print(f"\nTexto cifrado em base64: {b64_cipher_text}")
    
    print("-" * 100)




key = b'0123456789abcdef'  # chave de 16 bytes (128 bits)
message = b"oooooooooooooooooooooooooooooooo" # neste exemplo, vemos na saída do ECB dois blocos de 16 bytes iguais e um terceiro do padding

# message = b'a' * 10**9  # 1 GB; usado para teste de performance


modes = ['ECB', 'CBC', 'CFB', 'OFB', 'CTR']
for mode in modes:
    aes_encrypt(message, key, mode)
