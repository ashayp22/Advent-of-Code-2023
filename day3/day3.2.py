file1 = open('input2.txt', 'r')
Lines = file1.readlines()

mat = []

for line in Lines:
    row = []

    for c in line:
        if c != "\n":
            row.append(c)

    mat.append(row)

def is_part(i, j):
    if not (0 <= i < len(mat) and 0 <= j < len(mat[0])):
        return (0, 0)

    return (i, j) if mat[i][j] == "*" else (0, 0)

def is_part_num(i, j):
    total = (0, 0)

    for a, b in [(i-1, j), [i+1, j], (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
        p = is_part(a, b)
        total = (total[0] | p[0], total[1] | p[1])

    return total


sums = {}
nums = {}

for i in range(len(mat)):
    num = 0
    part = False
    for j in range(len(mat[i])):
        if mat[i][j].isnumeric():
            num = num*10 + int(mat[i][j])

            p = is_part_num(i, j)

            if p != (0, 0):
                part = p
        else:
            if num != 0 and part:
                # Add to sum and num for that part
                sums[part] = num if part not in sums else sums[part] * num
                nums[part] = 1 if part not in nums else 2
            num = 0
            part = False

    # Final check on num
    if num != 0 and part:
        # Add to sum for that part
        sums[part] = num if part not in sums else sums[part] * num
        nums[part] = 1 if part not in nums else 2

# find total
total = 0

print(sums)
print(nums)

for part in nums.keys():
    if nums[part] == 2:
        total += sums[part]

print(total)