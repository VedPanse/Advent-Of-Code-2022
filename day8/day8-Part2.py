import numpy

tree_group = []
with open('day8.txt') as file:
    temp = file.readline().strip()
    while temp != '':
        tree_group.append(temp)
        temp = file.readline().strip()

tree_60 = [[row[i] for row in tree_group] for i in range(len(tree_group[0]))]

visible_trees_list = [[[] for i in tree_group[0]] for j in tree_group]

for j in range(len(tree_group)):
    row = tree_group[j]
    for i in range(len(row)):
        lVis = 0
        for left in reversed(row[:i]):
            lVis += 1
            if left >= row[i]:
                break
        visible_trees_list[j][i].append(lVis)

        rightVisible = 0
        for right in row[i + 1:]:
            rightVisible += 1
            if right >= row[i]:
                break
        visible_trees_list[j][i].append(rightVisible)

for j in range(len(tree_60)):
    row = tree_60[j]
    for i in range(len(row)):
        lVis = 0
        for left in reversed(row[:i]):
            lVis += 1
            if left >= row[i]:
                break
        visible_trees_list[i][j].append(lVis)

        rightVisible = 0
        for right in row[i + 1:]:
            rightVisible += 1
            if right >= row[i]:
                break
        visible_trees_list[i][j].append(rightVisible)

maxScene = 0
for row in visible_trees_list:
    for ele in row:
        ele = numpy.prod(ele)
        if ele > maxScene:
            maxScene = ele
print(maxScene)
