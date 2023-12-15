file1 = open('input.txt', 'r')
Lines = file1.readlines()

platform = []

for line in Lines:
    if line[-1] == "\n":
        line = line[:-1]

    platform.append(line)

n = len(platform)
m = len(platform[0])

print(f"{n} {m}")

ans = 0

# Keep tilting, if we reach a state previously reached then we've found a loop and can jump to the end
for j in range(m):
    prev_i = -1
    curr_i = 0
    num_zero = 0

    col_sum = 0

    while curr_i < n:
        if platform[curr_i][j] == "O":
            num_zero += 1
        elif platform[curr_i][j] == "#":
            for add in range(num_zero):
                col_sum += n - (prev_i + 1) - add

            prev_i = curr_i
            num_zero = 0

        curr_i += 1

    for add in range(num_zero):
        col_sum += n - (prev_i + 1) - add

    ans += col_sum
    print(f"col_sum: {col_sum}")

print(f"Answer: {ans}")