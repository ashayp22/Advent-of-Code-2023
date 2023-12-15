file1 = open('input1.txt', 'r')
Lines = file1.readlines()

total = 0

card_number = []

n = len(Lines)

for card in Lines:
    s = card.split(" | ")

    left = s[0].split(" ")[2:]

    win_cards = set()

    for c in left:
        if c.isnumeric():
            win_cards.add(c)

    right = s[1].split(" ")

    points = 0

    for my_card in right:
        card_to_check = my_card

        if len(card_to_check) >= 2 and card_to_check[-1] == "\n":
            card_to_check = card_to_check[0:-1]

        if not card_to_check.isnumeric():
            continue

        if card_to_check in win_cards:
            points += 1

    card_number.append(points)

num_copies = [1 for _ in range(n)]
total = 0

for i in range(n):
    total += num_copies[i]

    for j in range(card_number[i]):
        num_copies[i+j+1] += num_copies[i]

print(total)