file1 = open('input1.txt', 'r')
Lines = file1.readlines()

init_seeds = []
maps = [[], [], [], [], [], [], []]

map_idx = -1

for line in Lines:
    if len(init_seeds) == 0:
        split_line = line.split(" ")[1:]
        split_line[-1] = split_line[-1][0:-1] # trim whitespace

        num = -1
        r = -1

        for a in split_line:
            if num == -1:
                num = int(a)
            else:
                r = int(a)

                init_seeds.append((num, r))
                num = -1

    elif line == "\n":
        map_idx += 1
    elif "map:" in line:
        continue
    else:
        # This is a range
        rng = line.split(" ")
        dest = int(rng[0])
        src = int(rng[1])

        r = rng[2]

        if r[-1] == "\n":
            r = int(r[0:-1])
        else:
            r = int(r)

        maps[map_idx].append((dest, src, r))


min_m = float('inf')

print(init_seeds)

for loc in range(100000000):
    val = loc
    for i in range(7):
        new_val = val

        for dest, src, r in maps[6-i]:
            if dest <= val < dest + r:
                new_val = src + (val - dest)
                break

        val = new_val

    for src, r in init_seeds:
        if src <= val < src + r:
            print(loc)
            exit(1)