minimal1 = int(input('Enter the minimum value Counter#1: '))
maximal1 = int(input('Enter the maximum value Counter#1: '))
minimal2 = int(input('Enter the minimum value Counter#2: '))
maximal2 = int(input('Enter the maximum value Counter#2: '))

class Counter:

    def __init__(self, minimal: int, maximal: int):
        self.minimal = minimal
        self.maximal = maximal
        self.current = minimal

    def increment(self):
        self.current += 1
        if self.current > self.maximal:
            self.current = self.minimal

    def __repr__(self):
        return f'Counter({self.minimal=}, {self.maximal=}), current position={self.current=}'

    def __eq__(self, other):
        return self.current == other.current

    def __lt__(self, other):
        return self.current < other.current

    def __gt__(self, other):
        return self.current > other.current


if __name__ == '__main__':
    counter1 = Counter(minimal=minimal1, maximal=maximal1)
    counter2 = Counter(minimal=minimal2, maximal=maximal2)
    print(counter1)
    print(counter2)
    if maximal1 > maximal2:
        if minimal1 < minimal2:
            llen = maximal1 - minimal1
        else:
            llen = maximal1 - minimal2
    else:
        if minimal1 < minimal2:
            llen = maximal2 - minimal1
        else:
            llen = maximal2 - minimal2
    for _ in range(llen):
        counter1.increment()
        counter2.increment()
        print(f'Counter#1 is equals Counter#2 - {counter1 == counter2}', f'{counter1.current=}, {counter2.current=}')
        print(f'Counter#1 is less than Counter#2 - {counter1 < counter2}', f'{counter1.current=}, {counter2.current=}')
        print(f'Counter#1 is greater than Counter#2 - {counter1 > counter2}', f'{counter1.current=}, {counter2.current=}')
    print('Check resetting')
    counter1.increment()
    counter2.increment()
    print( counter1.current)
    print( counter2.current)

print()