file1 = open('input.txt', 'r')
Lines = file1.readlines()

all_ponds = []
curr_pond = []

for line in Lines:
    if line == "\n":
        all_ponds.append(curr_pond)
        curr_pond = []
    else:
        row = []

        for a in line:
            if a == "#":
                row.append(1)
            elif a == ".":
                row.append(0)

        curr_pond.append(row)

all_ponds.append(curr_pond)

def findCount(mat, exclude=None):
    n = len(mat)
    m = len(mat[0])

    # Check for a vertical line reflection
    ans = set(i for i in range(1, m))
    curr_row = 0

    if exclude:
        ans.remove(exclude)

    while len(ans) > 0 and curr_row < n:
        for pot_div in range(1, m):
            left = mat[curr_row][:pot_div][::-1]
            right = mat[curr_row][pot_div:]

            min_len = min(len(left), len(right))

            if left[:min_len] != right[:min_len]:
                if pot_div in ans:
                    ans.remove(pot_div)

        curr_row += 1

    first = list(ans)

    if len(first) > 0:
        return first[0]

    return 0

ans = 0

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def getOriginal(pond):
    vert = findCount(pond)
    hort = findCount(transpose(pond))

    if vert > 0:
        return (vert, "V")

    if hort > 0:
        return (hort, "H")

    return (-1, "H")

def fixSmudge(pond):
    orig_ans, type = getOriginal(pond)
    # print(f"{orig_ans} {type}")

    for i in range(len(pond)):
        for j in range(len(pond[0])):
            pond[i][j] = 1 if pond[i][j] == 0 else 0
            # print(pond)

            vert = findCount(pond, exclude=orig_ans if type == "V" else None)
            hort = findCount(transpose(pond), exclude=orig_ans if type == "H" else None)

            # print(f"{i} {j}")
            # print(f"{hort}")

            if vert > 0:
                return vert

            if hort > 0:
                return hort * 100

            pond[i][j] = 1 if pond[i][j] == 0 else 0

counter = 0
for pond in all_ponds:
    print(f"{counter}")
    ans += fixSmudge(pond)
    counter += 1

print(f"Answer: {ans}")

