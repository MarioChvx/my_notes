
class fibonacci():

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return 0
        elif self.counter == 1:
            self.counter += 1
            return 1
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            if not self.max or self.aux <= self.max:
                return self.aux
            else:
                raise StopIteration

if __name__ == '__main__':
    fibo = fibonacci(8889)
    for number in fibo:
        print(number)