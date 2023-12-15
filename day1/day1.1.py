file1 = open('input1.txt', 'r')
Lines = file1.readlines()

total = 0

for line in Lines:
    num = 0

    first = -1

    for a in line:
        if a.isnumeric():
            last = int(a)

            if first == -1:
                first = int(a)

    total += first*10 + last

print(total)