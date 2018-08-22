def english_test(bytes_):
    # From http://www.data-compression.com/english.html
    """
    Gives a score based on the possibility of the string being in English
    """
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
    """
     Returns a XOR'd bytes result between two byte strings
    """
    return bytes([x ^ y for x, y in zip(a, b)])

def xor_repeated_key(message, key):
    """
    Divides a byte string by the length of a given byte string key
    and XOR each chunk using the key
    """
    repeats, remainder = divmod(len(message), len(key))
    return xor_bytes(message, bytes(key * repeats + key[:remainder]))

def brute_force_single_char_xor(cypher):
    """
    Takes a byte string and test all the possible possible values
    between 0 and 255, then assigns a score.
    Returns a bytes result with the best score.
    """
    key_range = range(255)
    best_score = 0
    result = bytes()
    for key in key_range:
        try:
            hexed_message = xor_repeated_key(cypher, bytes.fromhex(str(key)))
            new_score = english_test(hexed_message.decode("ascii"))
            if new_score > best_score:
                best_score = new_score
                result = hexed_message
        except:
            pass

    return result

def find_distance(bytes_1, bytes_2):
    """
     Expects byte strings as arguments
     Returns an integer
     This takes two string and gives the number of bits
     that differs between them
    """
    distance = 0
    for x, y in zip(bytes_1, bytes_2):
        difference = x ^ y
        distance += sum([1 for bit in bin(difference) if bit == "1"])
    return distance


