import cmath, math

file1 = open('input1.txt', 'r')
Lines = file1.readlines()

times = [63789468]
distance = [411127420471035]

# for line in Lines:
#     if len(times) == 0:
#         for t in line.split(" ")[1:]:
#             a = t.strip()
#
#             if len(a) >= 2 and a[-1] == '\n':
#                 a = a[0:-1]
#
#             if a.isnumeric():
#                 times.append(int(a))
#     else:
#         for t in line.split(" ")[1:]:
#             a = t.strip()
#             if a.isnumeric():
#                 distance.append(int(a))
#
# print(times)
# print(distance)

won = 1

for i in range(len(distance)):
    t = times[i]
    dist = distance[i]

    a = -1
    b = t
    c = -dist

    d = (b ** 2) - (4 * a * c)

    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)

    upper = math.floor(sol1-0.001)
    lower = math.ceil(sol2+0.001)

    print(f"lower: {lower}")
    print(f"upper: {upper}")

    if t-1 < lower:
        # Too low
        continue
    else:
        nums = min(upper, t-1) - lower + 1
        print(f"nums: {nums}")
        won *= nums

print(won)

