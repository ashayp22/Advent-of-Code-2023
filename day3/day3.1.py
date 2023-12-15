file1 = open('input1.txt', 'r')
Lines = file1.readlines()


mat = []

for line in Lines:
    row = []

    for c in line:
        if c != "\n":
            row.append(c)

    mat.append(row)

total = 0

def is_part(i, j):
    if not (0 <= i < len(mat) and 0 <= j < len(mat[0])):
        return False

    return not mat[i][j].isnumeric() and mat[i][j] != "."

def is_part_num(i, j):
    return is_part(i-1, j) or is_part(i+1, j) or is_part(i, j-1) \
           or is_part(i, j+1) or is_part(i-1, j-1) or is_part(i-1, j+1) \
           or is_part(i+1, j-1) or is_part(i+1, j+1)

for i in range(len(mat)):
    num = 0
    part = False
    for j in range(len(mat[i])):
        if mat[i][j].isnumeric():
            num = num*10 + int(mat[i][j])

            if is_part_num(i, j):
                # print(f"{i}, {j}")
                part = True
        else:
            if num != 0 and part:
                # print(num)
                total += num
            num = 0
            part = False

    # Final check on num
    if num != 0 and part:
        # print(num)
        total += num

print(total)