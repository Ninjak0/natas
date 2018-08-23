import base64
from Cryptodome.Cipher import AES

with open('7.txt') as input_file:
    text = input_file.readlines()
    ciphertext = base64.b64decode("".join(text))

key = b"YELLOW SUBMARINE"

obj = AES.new(key, AES.MODE_ECB)
plaintext = obj.decrypt(ciphertext)

print(plaintext.decode("ascii"))

