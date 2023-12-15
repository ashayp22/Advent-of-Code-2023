file1 = open('input.txt', 'r')
Lines = file1.readlines()

history = []

for line in Lines:
    if line[-1] == '\n':
        line = line[0:-1]

    history.append([int(a) for a in line.split(" ")])

ans = 0

for hist in history:
    rows = [hist]
    prev = 0

    # build down
    while True:
        new_row = []

        all_zero = True

        for i in range(len(rows[prev])-1):
            diff = rows[prev][i+1]-rows[prev][i]
            all_zero = diff == 0 and all_zero
            new_row.append(diff)

        rows.append(new_row)

        prev += 1

        if all_zero:
            break

    # build up
    n = len(rows)
    num = 0

    for j in range(1, n):
        num = rows[n-1-j][0] - num

    ans += num

print(ans)