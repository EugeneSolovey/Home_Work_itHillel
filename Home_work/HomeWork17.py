cities = input("Enter cities separated by a space: ").lower().split()
all_results = []  # Список всех комбинаций


def cities_combinations(cities):
    '''
    Функция получения всех комбинаций
    :param cities: Список городов
    :return: Комбинация городов
    '''
    cities_copy = list(set(cities))
    combination = []

    for city in cities_copy:
        for _ in cities_recursions([city], cities_copy, [city]):
            if _:
                combination.append(_)

    combination.sort(key=lambda char: len(char))
    return combination


def cities_recursions(current_list, copy, used):
    '''
    Функция получения комбинаций для одного из городов
    :param current_list: Список городов для комбинации
    :param copy: Копия списка городов
    :param used: Список использованных городов
    :return: Список комбинаций
    '''
    last_city = current_list[-1]
    cur_len = len(used)
    iter_next = (next_city  # Города, которые начинаются на последнюю букву последнего города в списке current_list
                 for next_city in copy
                 if next_city not in used
                 if next_city[0] == last_city[-1]
                 )
    for item in iter_next:
        new_current_list = current_list + [item]
        used.append(item)
        yield new_current_list
        yield from cities_recursions(new_current_list, copy, used)

    new_len = len(used)
    if new_len == cur_len:
        return []


def main():
    '''
    Функция получения всех комбинаций
    :return: Максимально длинная комбинация городов
    '''
    global cities, all_results

    for one_of_combination in cities_combinations(cities):
        all_results.append(one_of_combination)
    max_combination = max(all_results, key=len)
    return max_combination


result_game = main()
for _ in result_game:
    _ = _.capitalize()
    print(_, end=' ')
print()
print("Maximal combination is", len(result_game), "cities")
