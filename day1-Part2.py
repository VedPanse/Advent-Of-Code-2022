import numpy

fs = open("/Users/vedpanse/Advent of Code/2022/day1/day1.txt", "r")
data = fs.read().split("\n\n")
fs.close()

ind_list = []
int_lst = []


for item in data:
    lst = item.split('\n')
    int_lst.append([int(k) for k in lst])

sorted_list = [sum(items) for items in int_lst]
sorted_list.sort()
print(sorted_list[-1] + sorted_list[-2] + sorted_list[-3])
