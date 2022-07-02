# Anonymous functions


def get_currency_amount(currency_a, rate=29.5):  # arguments list in ()
    # optional docstring
    """
    Returns the amount of money in the currency.
    """
    return currency_a // rate


# Identical to:
get_currency_amount = lambda currency_a, rate: currency_a // rate


def get_family_name(name):
    return name.split(" ")[-1]

get_family_name = lambda name: name.split()[-1]

# Family-name sorting
names = ["Aleksey Ivanov", "Ivan Sidorov", "Ivan Alekseev"]
# names.sort(key=get_family_name)
names.sort(key=lambda name: name.split()[-1])
print(names)


# Imperative
surnames = list(get_family_name(name) for name in names)
print(surnames)


# Declaritive (map)
surnames_iter = map(get_family_name, names)
print(surnames_iter, type(surnames_iter))
print(next(surnames_iter))
surnames = list(surnames_iter)
print(surnames)


def get_fahrenheit_hours(celsius_hours):
    return list(map(lambda c: c * 9 / 5 + 32, celsius_hours))


celsius = 30
# print(get_fahrenheit_hours([celsius])[0])


def get_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def get_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


#fahr = print_fahrenheit(50)
#print(fahr)



weather_celsius = [15, 20, 30, 31, 29, 25, 22]
weather_fahrenheit = list(map(lambda c: c * 9 / 5 + 32, weather_celsius))
#weather_fahrenheit = [get_fahrenheit(celsius) for celsius in weather_celsius]

print(weather_fahrenheit)


# filter

def get_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

temperature_cities = {
    "Kyiv": (15, 20, 30),
    "Warsaw": (14, 21, 27),
    "Oslo": (12, 17, 24),
    "Vorkuta": (-10, -5, -3),
}

print(get_average_temperature(temperature_cities["Kyiv"]))

negative_temperature_cities = {
    city: temperature
    for city, temperature in temperature_cities.items()
    if get_average_temperature(temperature) < 0
}
print(negative_temperature_cities)


def is_negative_temp(temp_pair):
    temp = temp_pair[1]
    return get_average_temperature(temp) < 0

negative_temp_iter = filter(is_negative_temp, temperature_cities.items())
print(negative_temp_iter, dict(negative_temp_iter))


print(range(0, 100000, 1))
print(list(range(0, 10)))


def custom_range(start, stop, step):
    while start < stop:
        yield start
        start += step

c_range = custom_range(0, 100, 1)
print(type(c_range), c_range)

#print(next(c_range))
#print(next(c_range))

for _ in range(20):
    print(next(c_range))

from_20_to_99 = list(c_range)
print(from_20_to_99)

#print(custom_range(0, 1000, 1))