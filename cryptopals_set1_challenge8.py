with open('8.txt') as input_file:
    ciphertext = input_file.readlines()

def find_ECB(ciphertext):
    for line in ciphertext:
        chunks = [line[i:i+16] for i in range(0, len(line), 16)]
        for chunk in chunks:
            reps = 0
            for chunker in chunks:
                if chunk == chunker:
                    reps += 1
            if reps > 1:
                return "".join(chunks)


print(find_ECB(ciphertext))