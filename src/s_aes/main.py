from encrypt_saes import encrypt_saes

message = input("Digite a mensagem a ser cifrada: ")
key = input("Digite a chave em hexadecimal (e.g.: 0xA73B): ")
key = ["0x"+key[i] for i in range(2, len(key))]
key = [int(k, 16) for k in key]

encrypt_saes(message, key)