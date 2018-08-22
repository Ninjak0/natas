import base64
from utils import find_distance

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

    possible_keys = sorted(average_distances, key=lambda x: x['avg distance'])[:3]

    return [possible_key["key"] for possible_key in possible_keys]



print(guess_key_size(ciphertext))