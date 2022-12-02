score = 0
WEAKNESS = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

POINTS = {
    "Y": 2,
    "X": 1,
    "Z": 3,
}

COMPARISON = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

fs = open("day2.txt", "r")
data = fs.read().split("\n")
fs.close()

for items in data:
    my_list = items.split(" ")
    score += POINTS[my_list[1]]
    if my_list[1] == COMPARISON[my_list[0]]:
        score += 3
    elif my_list[1] == WEAKNESS[my_list[0]]:
        score += 6

print(score)
