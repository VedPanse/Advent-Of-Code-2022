COUNT = 0

fs = open("day4.txt", "r")
data = fs.read().split("\n")
fs.close()

pairWise = []

for items in data:
    pairWise.append(items.split(","))


for items in pairWise:
    first = items[0].split("-")
    second = items[1].split("-")
    range_first = [k for k in range(int(first[0]), int(first[-1]) + 1)]
    range_second = [k for k in range(int(second[0]), int(second[-1]) + 1)]
    if all(x in range_first for x in range_second) or all(x in range_second for x in range_first):
        COUNT += 1


print(COUNT)
