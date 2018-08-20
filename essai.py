message = b'the cat in the hat'
possible_key_length = 3
for i in range(possible_key_length):
    block = b''
    for j in range(i, len(message), possible_key_length):
         block += bytes([message[j]])
         print(block)