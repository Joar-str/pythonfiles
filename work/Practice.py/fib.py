class Fibonacci():
    def __init__(self, n):
        self._sequence = [0]*(n)

        if n >= 1:
            self._sequence[0] = 1
        if n >= 2:
            self._sequence[1] = 1
        for i in range(2, n):
            self._sequence[i] = (self._sequence[i-1] + self._sequence[i-2])

    def __getitem__(self, index):
        return self._sequence[index-1]

if __name__ == "__main__":
    fib = Fibonacci(20)
    print(fib[3])