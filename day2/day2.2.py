file1 = open('input1.txt', 'r')
Lines = file1.readlines()

total = 0

def getNumColor(line):
    a = line.split(" ")

    num = int(a[1])
    color = a[2]

    if color[-1] == '\n':
        color = color[0:len(color)-1]

    return num, color


for line in Lines:
    first = line.split(":")

    game_id = int(first[0].split(" ")[1])

    games = first[1].split(";")

    is_valid = True

    dict = {"red": 0, "blue": 0, "green": 0}

    for game in games:
        game_split = game.split(",")
        for pulled in game_split:
            num, color = getNumColor(pulled)
            dict[color] = max(dict[color], num)

    total += dict["red"] * dict["blue"] * dict["green"]

print(total)