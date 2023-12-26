file1 = open('input1.txt', 'r')
Lines = file1.readlines()

hailstones = []

for line in Lines:
    if line[-1] == "\n":
        line = line[0:-1]

    split_line = line.split(" @ ")
    pos = split_line[0].split(", ")
    vel = split_line[1].split(", ")

    hailstones.append((int(pos[0]), int(pos[1]), int(pos[2]), int(vel[0]), int(vel[1]), int(vel[2])))

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

n = len(hailstones)

MIN = 200000000000000
MAX = 400000000000000

ans = 0

for i in range(n):
    for j in range(i+1, n):
       l1 = line((hailstones[i][0], hailstones[i][1]), (hailstones[i][0] + hailstones[i][3], hailstones[i][1] + hailstones[i][4]))
       l2 = line((hailstones[j][0], hailstones[j][1]), (hailstones[j][0] + hailstones[j][3], hailstones[j][1] + hailstones[j][4]))

       res = intersection(l1, l2)

       if res:
           x, y = res
           if MIN <= x <= MAX and MIN <= y <= MAX \
                   and (x >= hailstones[i][0] if hailstones[i][3] >= 0 else x <= hailstones[i][0])\
                   and (y >= hailstones[i][1] if hailstones[i][4] >= 0 else y <= hailstones[i][1])\
                   and (x >= hailstones[j][0] if hailstones[j][3] >= 0 else x <= hailstones[j][0]) \
                   and (y >= hailstones[j][1] if hailstones[j][4] >= 0 else y <= hailstones[j][1]):
               ans += 1

print(f"Answer: {ans}")
