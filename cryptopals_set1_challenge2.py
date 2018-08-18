

def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


string_1 = "1c0111001f010100061a024b53535009181c"
string_2 = "686974207468652062756c6c277320657965"

bytes_1 = bytes.fromhex(string_1)
bytes_2 = bytes.fromhex(string_2)

xored = xor_bytes(bytes_1, bytes_2)
print(xored)
print(xored.hex())

