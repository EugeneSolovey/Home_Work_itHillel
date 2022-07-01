cities = input("Enter cities separated by a space: ").lower().split()


def get_cities_seq(cities):
    c_copy = list(set(cities))                          # copy of cities
    result = []                                         # result list

    for c in c_copy:                                    # for each city in cities
        for l in get_cities_rec([c], c_copy, [c]):      # get all possible combinations
            if l:                                       # if list is not empty
                result.append(l)                        # add to result list

    result.sort(key=lambda l: len(l))                   # sort by length
    print('result', result)                             # print result
    return result                                       # return result


def get_cities_rec(current_list, copy, used):            # recursive function
    c = current_list[-1]                                 # get last city in current list
    cur_len = len(used)                                  # get current length of used list
    iter_next = (nc for nc in copy if nc not in used if nc[0] == c[-1]) # get next cities
    for item in iter_next:                               # for each next city
        to_yield = current_list + [item]                 # add to current list
        used.append(item)                                # add to used list
        yield to_yield                                   # yield current list
        yield from get_cities_rec(to_yield, copy, used)  # get all possible combinations

    new_len = len(used)                                  # get new length of used list
    if new_len == cur_len:                               # if new length is equal to old length
        return []                                        # return empty list


def main():                                             # main function
    global cities                                       # global cities
    for comb in get_cities_seq(cities):                 # for each combination
        print(*comb)                                    # print combination


if __name__ == '__main__':
    main()