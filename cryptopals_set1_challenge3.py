

string1 = (bin(int("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", 16))[2:])
string2 = (bin(int(ord("A")))[2:])
string3 = ""
while len(string1) < len(string3):
    string3 = string3 + string2
    print(string3)
result = ""

for k, i in enumerate(string1):
    compared = int(i) ^ int(string3[k])
    result += str(compared)

print(hex(int(result, 2))[2:])