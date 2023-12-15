file1 = open('input.txt', 'r')
Lines = file1.readlines()

all_strings = Lines[0].split(",")

ans = 0

def getHash(str):
    val = 0
    for c in str:
        val += ord(c)
        val *= 17
        val = val % 256

    return val


for str in all_strings:
    ans += getHash(str)

print(f"Answer: {ans}")