alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# define reverse lookup dict
PLACE_VALUE = dict([(x[1], x[0]) for x in enumerate(alfa)])

common = []
fs = open("day3.txt", "r")
data = fs.read().split("\n")
fs.close()

all_first = []
all_second = []

for test_str in data:
    all_first.append(test_str[0:len(test_str) // 2])
    all_second.append(test_str[len(test_str) // 2 if len(test_str) % 2 == 0
                               else ((len(test_str) // 2) + 1):])

for items in all_first:
    lst_items = list(items)
    second_items = list(all_second[all_first.index(items)])
    common.append([k for k in lst_items if k in second_items])

COMMON_SET = [k[0] for k in common]

print(sum([PLACE_VALUE[item] + 1 for item in COMMON_SET]))
