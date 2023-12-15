file1 = open('input.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    split_line = line.split(" ")
    first = split_line[0]
    other = split_line[1].split(",")

    if other[-1][-1] == "\n":
        other[-1] = other[-1][0:-1]

    second = [int(r) for r in other]

    rows.append((first + "?" + first + "?" + first + "?" + first + "?" + first, second + second + second + second + second))


def mempFNP(record, nums):
    n = len(record)
    m = len(nums)

    FNP = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # Base cases
    FNP[n][m] = 1

    for j in range(m):
        FNP[n][j] = 0

    for i in range(n):
        FNP[i][m] = 0 if "#" in record[i:] else 1

    i = n-1

    while i >= 0:
        j = m-1
        while j >= 0:
            curr_num = nums[j]
            matches = 0

            if "." not in record[i:i + curr_num]:
                # Enough space left in record
                if curr_num + i <= n and j == m - 1:
                    matches += FNP[i + curr_num][j + 1]
                elif curr_num + i + 1 <= n and "#" != record[i + curr_num]:
                    matches += FNP[i + curr_num + 1][j + 1]

            # Skip the current val
            if record[i] != "#":
                matches += FNP[i + 1][j]

            FNP[i][j] = matches

            j -= 1
        i -= 1

    return FNP[0][0]

ans = 0

counter = 0
for record, nums in rows:
    poss = mempFNP(record, nums)
    ans += poss
    print(f"{counter}")
    counter += 1

print(ans)

