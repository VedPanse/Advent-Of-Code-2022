fs = open("day6.txt", "r")
data = list(fs.read())
fs.close()

def func():
    for ind in range(0, len(data)):
        lst = [data[ind], data[ind + 1], data[ind + 2], data[ind + 3]]
        sets = list(set(lst))
        lst.sort()
        sets.sort()
        if lst == sets:
            return ind + 4


print(func())

