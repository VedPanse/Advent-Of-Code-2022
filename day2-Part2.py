score = 0
WEAKNESS = {
    "A": "B",
    "B": "C",
    "C": "A"
}

POINTS = {
    "Y": 3,
    "X": 0,
    "Z": 6,
}

COMPARISON = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

POINTS_X = {
    "A": 1,
    "B": 2,
    "C": 3
}

STRENGTHS = {
    "A": "C",
    "C": "B",
    "B": "A"
}

fs = open("day2.txt", "r")
data = fs.read().split("\n")
fs.close()

for items in data:
    my_list = items.split(" ")
    score += POINTS[my_list[1]]

    if my_list[1] == "Y":
        score += POINTS_X[my_list[0]]
    elif my_list[1] == "Z":
        score += POINTS_X[WEAKNESS[my_list[0]]]
    else:
        score += POINTS_X[STRENGTHS[my_list[0]]]

print(score)
