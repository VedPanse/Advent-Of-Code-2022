def build_directories(d, data, prev):
    while data:
        cmd = data.pop(0)
        if cmd == "$ ls":
            while data and not data[0].startswith("$"):
                a, b = data.pop(0).split(" ")
                d[prev + (b,)] = {} if a == "dir" else int(a)
        elif cmd.endswith(".."):
            return
        else:
            c = cmd.split(" ")[-1]
            p = prev + (c,)
            build_directories(d[p], data, prev + p)
    return d


def find_total_space_per_dir(d, key):
    current_sum = 0
    for k, v in d.items():
        if isinstance(v, int):
            current_sum += v
        else:
            current_sum += find_total_space_per_dir(v, k)
    total_space[key] = current_sum
    return current_sum


with open("day7.txt", "r") as file:
    data = file.read().splitlines()[1:]
    d = {"/": {}}
    directories = build_directories(d["/"], data, ("/",))
    total_space = {}
    find_total_space_per_dir(directories, key="/")
    print(sum(v for v in total_space.values() if v <= 100000))
