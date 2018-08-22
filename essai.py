from utils import find_distance, brute_force_single_char_xor, english_test, xor_repeated_key

def guess_key_size(ciphertext):
    average_distances = []
    for keysize in range(2, 5):
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

    possible_key_lengths = sorted(average_distances, key=lambda x: x['avg distance'])[:2]



message = b"""0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

print(guess_key_size(message))
