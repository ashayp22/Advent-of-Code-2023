file1 = open('input.txt', 'r')
Lines = file1.readlines()

platform = []

TOTAL_CYCLES = 1000000000

for line in Lines:
    if line[-1] == "\n":
        line = line[:-1]

    platform.append(line)

def rotate90Clockwise(mat):
    A = [[r for r in row] for row in mat]

    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

    return ["".join(row) for row in A]

def printPlatform(platform):
    for row in platform:
        print(row)
    print("-----------------")

def moveWest(plat):
    n = len(plat)
    m = len(plat[0])

    for i in range(n):
        prev_j = -1
        curr_j = 0
        num_zero = 0

        while curr_j < m:
            if plat[i][curr_j] == "O":
                num_zero += 1
            elif plat[i][curr_j] == "#":
                plat[i] = plat[i][:prev_j+1] + num_zero * "O" + "." * (curr_j - (prev_j + 1) - num_zero) + plat[i][curr_j:]

                prev_j = curr_j
                num_zero = 0

            curr_j += 1

        plat[i] = plat[i][:prev_j + 1] + num_zero * "O" + "." * (curr_j - (prev_j + 1) - num_zero) + plat[i][curr_j:]


# Keep tilting, if we reach a state previously reached then we've found a loop and can jump to the end
def fullCycle(c):
    p = [row for row in c]

    moveWest(p)
    west = rotate90Clockwise(p)
    moveWest(west)
    south = rotate90Clockwise(west)
    moveWest(south)
    east = rotate90Clockwise(south)
    moveWest(east)
    north = rotate90Clockwise(east)
    return north

def calculateLoad(platform):
    total = 0
    n = len(platform)
    m = len(platform[0])

    for i in range(n):
        for j in range(m):
            if platform[i][j] == "O":
                total += n - i

    return total

def getPlatformHash(platform):
    hash = ""

    for row in platform:
        hash += row

    return hash

found = {}
num_to_platform = {}

northPlatform = rotate90Clockwise(rotate90Clockwise(rotate90Clockwise(platform)))

# Add the starting platform
start_hash = getPlatformHash(northPlatform)
found[start_hash] = 0
num_to_platform[0] = northPlatform

start = -1

numCycles = 0

while numCycles < TOTAL_CYCLES:
    northPlatform = fullCycle(northPlatform)
    cycle_hash = getPlatformHash(northPlatform)

    numCycles += 1

    if cycle_hash in found:
        # Found a pattern
        start = found[cycle_hash]
        break
    else:
        found[cycle_hash] = numCycles
        num_to_platform[numCycles] = northPlatform

print(f"numCycles: {numCycles}")
print(f"start: {start}")

cycle_length = numCycles - start
print(f"cycle_length: {cycle_length}")

cycles_left = TOTAL_CYCLES - numCycles
correct_cycle = start + cycles_left % cycle_length

# Don't forget to rotate back facing north
ans_cycle = rotate90Clockwise(num_to_platform[correct_cycle])

printPlatform(ans_cycle)

ans = calculateLoad(ans_cycle)
print(f"Answer: {ans}")