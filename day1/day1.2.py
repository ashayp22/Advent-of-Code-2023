file1 = open('input2.txt', 'r')
Lines = file1.readlines()

total = 0

def strToNum(str):
    if str == "one":
        return 1
    elif str == "two":
        return 2
    elif str == "three":
        return 3
    elif str == "four":
        return 4
    elif str == "five":
        return 5
    elif str == "six":
        return 6
    elif str == "seven":
        return 7
    elif str == "eight":
        return 8
    elif str == "nine":
        return 9

    return -1

total = 0

for line in Lines:
    n = len(line)
    first = -1
    last = -1

    for i in range(n):
        if line[i].isnumeric():
            last = int(line[i])

            if first == -1:
                first = int(line[i])

        for j in range(6):
            if i+j >= n:
                continue

            num = strToNum(line[i:i+j])

            if num != -1:
                last = num

                if first == -1:
                    first = num

    a = first*10 + last
    print(a)
    total += a

print(total)