fs = open("day6.txt", "r")
data = list(fs.read())
fs.close()


def func():
    for ind in range(0, len(data)):
        lst = [data[ind], data[ind + 1], data[ind + 2], data[ind + 3], data[ind + 4], data[ind + 5], data[ind + 6], data[ind + 7], data[ind + 8], data[ind + 9], data[ind + 10], data[ind + 11], data[ind + 12], data[ind + 13]]
        sets = list(set(lst))
        lst.sort()
        sets.sort()
        if lst == sets:
            return ind + 14


print(func())
