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

    rows.append((first, second))

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

def findNumPossibilities(record, nums, i, j):
    n = len(record)
    m = len(nums)

    if i == n and j == m:
        # Good match
        return 1
    elif i == n and j < m:
        # At the end of record but nums still left
        return 0
    elif i < n and j == m:
        # Check if any # left
        return 0 if "#" in record[i:] else 1

    # Match nums[j] starting at record[i], else skip
    curr_num = nums[j]

    matches = 0

    if "." not in record[i:i+curr_num]:
        # Enough space left in record
        if curr_num + i <= n and j == m-1:
            add = findNumPossibilities(record, nums, i + curr_num, j + 1)
            matches += add
        elif curr_num + i + 1 <= n and "#" != record[i+curr_num]:
            add = findNumPossibilities(record, nums, i + curr_num + 1, j + 1)
            matches += add

    # Skip the current val
    if record[i] != "#":
        add = findNumPossibilities(record, nums, i+1, j)
        matches += add

    return matches

ans = 0

counter = 0
for record, nums in rows:
    poss = mempFNP(record, nums)
    ans += poss
    print(f"{counter}")
    counter += 1

print(f"Answer: {ans}")

