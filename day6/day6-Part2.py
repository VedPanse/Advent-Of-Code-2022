fs = open("day6.txt", "r")
data = list(fs.read())
fs.close()


def func():
    for ind in range(0, len(data)):
        lst = [data[ind + k] for k in range(14)]
        sets = list(set(lst))
        lst.sort()
        sets.sort()
        if lst == sets:
            return ind + 14


print(func())
