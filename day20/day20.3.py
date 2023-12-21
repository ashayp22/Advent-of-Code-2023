import math

lcm = [4091, 3767, 4001, 3761]

ans = 1
for n in lcm:
    ans = math.lcm(ans, n)

print(f"Answer: {ans}")