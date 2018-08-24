#Code for challenge 8

from collections import defaultdict

def repeated_blocks(buffer, block_length=16):
    reps = defaultdict(lambda: -1)
    for i in range(0, len(buffer), block_length):
        block = bytes(buffer[i:i + block_length])
        reps[block] += 1
    return sum(reps.values())

max_reps = 0
ecb_ciphertext = None

# The ciphertext is provided in a file named 8.txt
for ciphertext in list(open("8.txt", "r")):
    ciphertext = ciphertext.rstrip()
    reps = repeated_blocks(bytes(ciphertext, "utf-8"))
    if reps > max_reps:
        max_reps = reps
        ecb_ciphertext = ciphertext

print(ecb_ciphertext)