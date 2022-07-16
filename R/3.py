minimal = int(input('Введите минимальное значение счётчика: '))
maximal = int(input('Введите максимальное значение счётчика: '))

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


if __name__ == '__main__':
    counter = Counter(minimal=minimal, maximal=maximal)
    print( counter )
    for _ in range( maximal-minimal):
        counter.increment()
        print( counter.current )
    print( 'Check resetting' )
    counter.increment()
    print( counter.current )