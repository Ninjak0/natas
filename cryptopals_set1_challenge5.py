def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


def xor_repeated_key(message, key):
    repeats, remainder = divmod(len(message), len(key))
    return xor_bytes(message, bytes(key * repeats + key[:remainder]))


key = "ICE".encode("ascii")
string = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""".encode('ascii')

result_1 = xor_repeated_key(string, key).hex()

print(result_1)

result_2 = xor_repeated_key(bytes.fromhex(result_1), key)
print(result_2.decode("ascii"))