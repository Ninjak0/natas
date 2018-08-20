import binascii
import base64

def english_test(bytes_):
    # From http://www.data-compression.com/english.html
    freqs = {
        'a': 0.0651738,
        'b': 0.0124248,
        'c': 0.0217339,
        'd': 0.0349835,
        'e': 0.1041442,
        'f': 0.0197881,
        'g': 0.0158610,
        'h': 0.0492888,
        'i': 0.0558094,
        'j': 0.0009033,
        'k': 0.0050529,
        'l': 0.0331490,
        'm': 0.0202124,
        'n': 0.0564513,
        'o': 0.0596302,
        'p': 0.0137645,
        'q': 0.0008606,
        'r': 0.0497563,
        's': 0.0515760,
        't': 0.0729357,
        'u': 0.0225134,
        'v': 0.0082903,
        'w': 0.0171272,
        'x': 0.0013692,
        'y': 0.0145984,
        'z': 0.0007836,
        ' ': 0.1918182
    }
    score = 0
    for i in bytes_.lower():
        if i in freqs:
            score += freqs[i]
    return score

def find_distance(string_1, string_2):
    distance = 0
    bin_1 = bin(int(binascii.hexlify(string_1.encode("ascii")), 16))[2:]
    bin_2 = bin(int(binascii.hexlify(string_2.encode("ascii")), 16))[2:]
    for x, y in zip(bin_1, bin_2):
        if x != y:
            distance += 1
    return distance

with open('6.txt') as input_file:
    ciphertext = base64.b64decode(input_file.read())

def break_repeating_key_xor(ciphertext):
    average_distances = []
    for keysize in range(2, 41):
        distances_list = []

        chunks = [ciphertext.decode("ascii")[i:i+keysize] for i in range(0, len(ciphertext.decode("ascii")), keysize)]

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

    possible_key_lengths = sorted(average_distances, key=lambda x: x['avg distance'])[0]

    key = b""
    possible_key_length = possible_key_lengths["key"]

    for i in range(possible_key_length):
        block = b""
        for j in range(i, len(ciphertext), possible_key_length):
            block += bytes([ciphertext[j]])

    print(block)

break_repeating_key_xor(ciphertext)