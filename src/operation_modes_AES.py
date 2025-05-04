from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes

import base64
import time

def padding(text):
    # padding PKCS#7
    padding_len = 16 - (len(text) % 16) # se len(text) % 16 == 0, add 16 bytes
    return text + bytes([padding_len]) * padding_len # esses bytes são o valor do padding_len

def aes_encrypt(message, key, mode):

    if mode == 'ECB':
        start = time.time() # inicia o tempo de execução
        cipher = AES.new(key, AES.MODE_ECB) # cria o objeto AES com a chave e o modo
        cipher_text = cipher.encrypt(padding(message)) # cifra a mensagem com 
        b64_cipher_text = base64.b64encode(cipher_text).decode() # converte o texto cifrado para base64

    elif mode == 'CBC':
        start = time.time()
        init_vector = get_random_bytes(16) # vetor de inicialização com 16 bytes
        cipher = AES.new(key, AES.MODE_CBC, init_vector) # cria o objeto AES com a chave, modo e vetor de inicialização
        cipher_text = cipher.encrypt(padding(message))
        b64_cipher_text = base64.b64encode(init_vector + cipher_text).decode() # concatena o vetor de inicialização com o texto cifrado

    elif mode == 'CFB':
        start = time.time()
        init_vector = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CFB, init_vector)
        cipher_text = cipher.encrypt(message)
        b64_cipher_text = base64.b64encode(init_vector + cipher_text).decode()

    elif mode == 'OFB':
        start = time.time()
        init_vector = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_OFB, init_vector)
        cipher_text = cipher.encrypt(message)
        b64_cipher_text = base64.b64encode(init_vector + cipher_text).decode()

    elif mode == 'CTR':
        start = time.time()
        nonce = get_random_bytes(8) # nonce de 8 bytes
        cipher_textr = Counter.new(64, prefix=nonce) # contador de 64 bits com nonce 
        cipher = AES.new(key, AES.MODE_CTR, counter=cipher_textr) # cria o objeto AES com a chave, modo e contador
        cipher_text = cipher.encrypt(message)
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
