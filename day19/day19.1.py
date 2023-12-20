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

# print(workflows)
# print(parts)

total = 0

def getNext(part, curr):
    curr_conditions = workflows[curr]

    for condition in curr_conditions:
        if condition.skip:
            return condition.next

        if condition.is_less_than:
            if part[condition.var] < condition.val:
                return condition.next
        else:
            if part[condition.var] > condition.val:
                return condition.next


for part in parts:
    curr = "in"

    all = "in,"

    while curr != "R" and curr != "A":
        curr = getNext(part, curr)
        all += curr + ","

    # print(all)

    if curr == "A":
        total += part["x"] + part["m"] + part["a"] + part["s"]

print(f"Answer: {total}")