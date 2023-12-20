from dataclasses import dataclass

@dataclass
class Condition:
    is_less_than: bool
    next: str
    skip: bool
    val: int
    var: str

file1 = open('input1.txt', 'r')
Lines = file1.readlines()

workflows = {}
parts = []

add_parts = False

def eval_rule(str):
    condition = Condition(False, str, True, -1, "")

    if ":" not in str:
        return condition

    condition.skip = False

    split_str = str.split(":")

    condition.next = split_str[1]

    comparator = "<" if "<" in split_str[0] else ">"
    condition.is_less_than = comparator == "<"

    split_condition = split_str[0].split(comparator)

    condition.var = split_condition[0]
    condition.val = int(split_condition[1])

    return condition

for line in Lines:
    if line == "\n":
        add_parts = True
        continue

    # Remove new line
    if line[-1] == "\n":
        line = line[0:-1]

    if not add_parts:
        bracket_idx = line.index("{")
        name = line[0:bracket_idx]
        rest = line[bracket_idx+1:-1]
        rest = rest.split(",")

        conditions = [eval_rule(r) for r in rest]
        workflows[name] = conditions
    else:
        line = line[1:-1] # remove {}
        split_line = line.split(",")

        part = {}

        for val in split_line:
            split_val = val.split("=")
            part[split_val[0]] = int(split_val[1])

        parts.append(part)

# Setup parent rules and find
parent_rules = {}

queue = []

for name in workflows:
    conditions = workflows[name]

    for idx, condition in enumerate(conditions):
        child = condition.next

        if child in parent_rules:
            parent_rules[child].append((name, idx))
        else:
            parent_rules[child] = [(name, idx)]

        if condition.next == "A":
            queue.append((name, idx, {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}))

all_ranges = []

def satisfy_condition(ranges, condition):
    # If there is no condition, return
    if condition.skip:
        return

    if condition.is_less_than:
        # If m < 100, then we want to have <= 99
        ranges[condition.var][1] = min(ranges[condition.var][1], condition.val-1)
    else:
        # if m > 2, then we want to have >= 2
        ranges[condition.var][0] = max(ranges[condition.var][0], condition.val+1)

def unsatisfy_condition(ranges, condition):
    # If there is no condition, return
    if condition.skip:
        return

    if condition.is_less_than:
        # If m < 100, then we want to have >= 100
        ranges[condition.var][0] = max(ranges[condition.var][0], condition.val)
    else:
        # If m > 2, then we want to have <= 2
        ranges[condition.var][1] = min(ranges[condition.var][1], condition.val)

while len(queue) > 0:
    curr_name, curr_idx, ranges = queue.pop(0)

    # Update ranges based on current name

    # Satisfy current condition
    curr_condition = workflows[curr_name][curr_idx]
    satisfy_condition(ranges, curr_condition)
    curr_idx -= 1

    # Don't satisfy the previous conditions
    while curr_idx >= 0:
        unsatisfy_condition(ranges, workflows[curr_name][curr_idx])
        curr_idx -= 1

    if curr_name == "in":
        # Reached the beginning
        all_ranges.append(ranges)
    else:
        # Keep backtracking
        for parent, parent_idx in parent_rules[curr_name]:
            queue.append((parent, parent_idx, ranges))

# Determine total number of combinations of xmas
total = 0

for range in all_ranges:
    x, m, a, s = range["x"], range["m"], range["a"], range["s"]
    prod = (x[1] - x[0] + 1)
    prod *= (m[1] - m[0] + 1)
    prod *= (a[1] - a[0] + 1)
    prod *= (s[1] - s[0] + 1)
    total += prod

print(f"Answer: {total}")

