file1 = open('input1.txt', 'r')
Lines = file1.readlines()

cards = []

for line in Lines:
    card, num = line.split(" ")
    if len(num) >= 2 and num[-1] == "\n":
        num = num[0:-1]

    cards.append((card, int(num)))

def get_card_type(x):
    freq = {}

    num_j = 0

    for l in x:
        if l == "J":
            num_j += 1
        else:
            freq[l] = 1 if l not in freq else freq[l] + 1

    freq_list = sorted(freq.values(), reverse=True)

    if len(freq_list) == 0:
        freq_list = [num_j]
    else:
        freq_list[0] += num_j
        if freq_list[0] > 5:
            print("bad")

    if freq_list == [5]:
        return 7
    if freq_list == [4, 1]:
        return 6
    if freq_list == [3, 2]:
        return 5
    if freq_list == [3, 1, 1]:
        return 4
    if freq_list == [2, 2, 1]:
        return 3
    if freq_list == [2, 1, 1, 1]:
        return 2
    return 1

strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
strength = strength[::-1]

def compare(x, y):
    x_c = get_card_type(x[0])
    y_c = get_card_type(y[0])

    if x_c == y_c:
        for t in range(5):
            idx_x = strength.index(x[0][t])
            idx_y = strength.index(y[0][t])

            if idx_x != idx_y:
                return idx_x - idx_y

    return x_c - y_c


sorted_cards = cards
n = len(sorted_cards)

did_swap = True

counter = 0

while did_swap:
    i = 0
    did_swap = False
    while i < n-1:
        if compare(sorted_cards[i], sorted_cards[i+1]) > 0:
            temp = sorted_cards[i]
            sorted_cards[i] = sorted_cards[i+1]
            sorted_cards[i+1] = temp
            did_swap = True
            # print(f"{counter},{i}")

        i += 1
    counter += 1

total = 0

for j in range(len(sorted_cards)):
    total += (j+1) * sorted_cards[j][1]

print(total)
