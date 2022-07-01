cities = input("Enter cities separated by a space: ").lower().split()
all_res = []


def get_cities_seq(cities):
    c_copy = list(set(cities))
    result = []

    for c in c_copy:
        for l in get_cities_rec([c], c_copy, [c]):
            if l:
                result.append(l)

    result.sort(key=lambda l: len(l))
    return result


def get_cities_rec(current_list, copy, used):
    c = current_list[-1]
    cur_len = len(used)
    iter_next = (nc for nc in copy if nc not in used if nc[0] == c[-1])
    for item in iter_next:
        to_yield = current_list + [item]
        used.append(item)
        yield to_yield
        yield from get_cities_rec(to_yield, copy, used)

    new_len = len(used)
    if new_len == cur_len:
        return []


def main():
    global cities, all_res

    for comb in get_cities_seq(cities):
        all_res.append(comb)
    t = max(all_res, key=len)
    return t


t = main()
for _ in t:
    _ = _.capitalize()
    print(_, end=', ')



