import numpy as np


def parse08(filename):
    with open(filename) as f:
        return np.array([[int(n) for n in k.strip()] for k in f.readlines()])


def isVisible(i, j, gridLines):
    visT = sum([1 for t in gridLines[:j, i] if t >= gridLines[j][i]]) == 0
    visB = sum([1 for t in gridLines[j + 1:, i] if t >= gridLines[j][i]]) == 0
    visL = sum([1 for t in gridLines[j, :i] if t >= gridLines[j][i]]) == 0
    visR = sum([1 for t in gridLines[j, i + 1:] if t >= gridLines[j][i]]) == 0
    return visT or visB or visL or visR


def countVisible(grid):
    visible = np.zeros(grid.shape, int)
    for y in range(grid.shape[1]):
        for x in range(grid.shape[0]):
            visible[y][x] = isVisible(y, x, grid)
    return sum(sum(visible)), visible


grid0 = parse08("day8.txt")
grid = parse08("day8.txt")

sol1, visible = countVisible(grid)

print(sol1)
