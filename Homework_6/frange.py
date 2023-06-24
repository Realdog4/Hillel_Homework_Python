class Frange:
    def __init__(self, start, stop=None, step=1.0):
        if stop is None:
            start, stop = 0.0, float(start)
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        if self.step > 0:
            current = self.start
            while current < self.stop:
                yield current
                current += self.step
        elif self.step < 0:
            current = self.start
            while current > self.stop:
                yield current
                current += self.step

    def __reversed__(self):
        current = self.stop - self.step
        while current >= self.start:
            yield current
            current -= self.step


assert(list(Frange(5)) == [0, 1, 2, 3, 4])
assert(list(Frange(2, 5)) == [2, 3, 4])
assert(list(Frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(Frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(Frange(1, 5)) == [1, 2, 3, 4])
assert(list(Frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(Frange(0, 0)) == [])
assert(list(Frange(100, 0)) == [])

print('SUCCESS!')