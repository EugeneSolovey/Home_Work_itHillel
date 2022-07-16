'''Реализовать класс счетчика. В классе реализовать:
установки максимального значения (так же начального значения счётчика) при инициализации
увеличения счетчика на 1
возвращения текущего значения счётчика
методы сравнения и равенства двух счетчиков'''

class Counter:
    current=0
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def increase(self):

        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            return 'Out of range'


class CounterMetods(Counter):
    def __repr__(self):
        return f'{self.start=} {self.end=}'

    def __eq__(self):
        return self.start == self.current

    def __lt__(self):
        return self.start < self.current

    def __gt__(self):
        return self.start > self.current

    def __le__(self):
        return self.start <= self.current

    def __ge__(self):
        return self.start >= self.current

    def __ne__(self):
        return self.start != self.current


my_counter1 = CounterMetods(start=5, end=20)

print(my_counter1.increase())
print(my_counter1.increase())
print(my_counter1.increase())
print(my_counter1.increase())
print(my_counter1.increase())

