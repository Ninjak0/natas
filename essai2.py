
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

def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def xor_repeated_key(message, key):
    repeats, remainder = divmod(len(message), len(key))
    return xor_bytes(message, bytes(key * repeats + key[:remainder]))


def get_best_result(cypher):
    key_range = range(255)
    best_score = 0
    result = b""
    best_key = 0
    for key in key_range:
        try:
            hexed_message = xor_repeated_key(cypher, bytes.fromhex(str(key)))
            new_score = english_test(hexed_message.decode("ascii"))
            if new_score > best_score:
                best_score = new_score
                result = hexed_message
                best_key = key
        except:
            pass

    return result.decode("ascii"), best_key

cypher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hexed_cypher = bytes.fromhex(cypher)

print(get_best_result(hexed_cypher))

s1 = 110
s2 = 124

print(s1 ^ s2)