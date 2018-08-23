import base64
from utils import find_distance, brute_force_single_char_xor,xor_repeated_key

with open('6.txt') as input_file:
    text = input_file.readlines()
    ciphertext = base64.b64decode("".join(text))

def guess_key_size(ciphertext):
    average_distances = []
    for keysize in range(2, 41):
        distances_list = []

        chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]

        while True:
            try:
                chunk_1 = chunks[0]
                chunk_2 = chunks[1]

                new_distance = find_distance(chunk_1, chunk_2)

                distances_list.append(new_distance/keysize)

                del chunks[0]
                del chunks[1]
            except Exception as e:
                break

        result = {
            'key': keysize,
            'avg distance': sum(distances_list) / len(distances_list)
        }
        average_distances.append(result)

    possible_keys = sorted(average_distances, key=lambda x: x['avg distance'])[:1]

    return [possible_key["key"] for possible_key in possible_keys]

def break_into_blocks_to_get_key(ciphertext):
    key = b""
    keysizes = guess_key_size(ciphertext)
    for keysize in keysizes:
        for i in range(keysize):
            block = b""
            for j in ciphertext[i::keysize]:
                block += bytes([j])
            key += bytes([brute_force_single_char_xor(block)[1]])
        return key


cipher_key = break_into_blocks_to_get_key(ciphertext)
print(f"Cipher key: {cipher_key}")
print()
print(xor_repeated_key(ciphertext, cipher_key).decode("ascii"))