class Counter:

    def __init__(self, start=0):
        self._count = start
        self.__count = start

    def iter(self):
        self._count += 1
        self.__count += 1

    def get(self):
        return self._count



counter = Counter(100)

for _ in range(10):
    # counter._set(500)
    counter.iter()

print(f"{counter.get() = }")

print(f"{counter.__dict__ = }")
print(f"{counter._count = }")

print(f"{counter._Counter__count = }")



"""
private:
    _count: int

protected:
    ...

public:
    get
"""
