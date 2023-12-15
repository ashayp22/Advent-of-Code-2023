file1 = open('input.txt', 'r')
Lines = file1.readlines()

all_strings = Lines[0].split(",")

print(len(all_strings))

boxes = [[] for _ in range(256)]

def getHash(str):
    val = 0
    for c in str:
        val += ord(c)
        val *= 17
        val = val % 256

    return val

label_to_size = {}

for lens in all_strings:
    if "-" in lens:
        label = lens[0:lens.index("-")]
        box_idx = getHash(label)

        if label in boxes[box_idx]:
            # Found the label and must remove it
            idx = boxes[box_idx].index(label)
            boxes[box_idx].pop(idx)
            del label_to_size[(label, box_idx)]
    else:
        eq_idx = lens.index("=")
        label = lens[:eq_idx]
        num = int(lens[eq_idx+1:])
        box_idx = getHash(label)

        # Update the focal length
        label_to_size[(label, box_idx)] = num

        # Add to the box if it doesn't already exist
        if label not in boxes[box_idx]:
            boxes[box_idx].append(label)

print(label_to_size)
print(boxes)

ans = 0

for i in range(256):
    for j in range(len(boxes[i])):
        ans += (i+1) * (j+1) * label_to_size[(boxes[i][j], i)]

print(ans)





