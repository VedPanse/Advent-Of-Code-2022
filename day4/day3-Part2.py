alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# define reverse lookup dict
PLACE_VALUE = dict([(x[1], x[0]) for x in enumerate(alfa)])

fs = open("day3.txt", "r")
data = fs.read().split("\n")
fs.close()


# Yield successive n-sized
# chunks from l.
def divide_chunks(arr, chunk_size):
    # looping till length l
    for i in range(0, len(arr), chunk_size):
        yield arr[i:i + chunk_size]


# How many elements each
# list should have
n = 5

chunks = list(divide_chunks(data, 3))
REPEAT = []


def commonity(arr):
    first = list(arr[0])
    second = list(arr[1])
    third = list(arr[2])

    common = [k for k in first if k in second and k in third]
    return common[0]


priority = []
for items in chunks:
    priority.append(commonity(items))

priority_value = sum([PLACE_VALUE[item] + 1 for item in priority])
print(priority_value)
