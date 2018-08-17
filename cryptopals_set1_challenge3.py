
# This solution is far from complete

pass_key_high = "ETAOIN SHRDLU"
pass_key_low = "etaoin shrdlu"

string1 = (bin(int("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", 16))[2:])
string2 = (bin(int(ord("R")))[2:])
if len(string2) != 8:
    string2 = "0" + string2
result = ""

# for k, i in enumerate(string1):
#     compared = int(i) ^ int(string3[k])
#     result += str(compared)
#
# print(hex(int(result, 2))[2:])
