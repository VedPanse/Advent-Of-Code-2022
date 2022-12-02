import numpy

fs = open("/Users/vedpanse/Advent of Code/2022/day1/day1.txt", "r")
data = fs.read().split("\n\n")
fs.close()

ind_list = []
int_lst = []


for item in data:
    lst = item.split('\n')
    int_lst.append([int(k) for k in lst])

print(max([sum(items) for items in int_lst]))
