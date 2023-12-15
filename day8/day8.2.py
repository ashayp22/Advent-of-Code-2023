import math

file1 = open('input.txt', 'r')
Lines = file1.readlines()

left_right = []

graph = {}

curr = []

for line in Lines:
    if len(left_right) == 0:
        left_right = [0 if l == "L" else 1 for l in line[0:-1]]
    else:
        if line == "\n":
            continue

        split_line = line.split(" = ")
        to = split_line[0]
        f = split_line[1]

        if f[-1] == "\n":
            f = f[0:-1]

        split_f = f.split(", ")
        first = split_f[0][1:]
        second = split_f[1][0:-1]

        graph[to] = (first, second)

        if to[-1] == "A":
            curr.append(to)

print(curr)

def getNum(curr_num):
    steps = 0

    while True:
        for i in left_right:
            steps += 1

            curr_num = graph[curr_num][i]

            if curr_num[-1] == "Z":
                return steps

lcm = [getNum(c) for c in curr]
print(lcm)

ans = 1
for n in lcm:
    ans = math.lcm(ans, n)

print(ans)