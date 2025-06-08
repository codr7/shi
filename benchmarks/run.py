from timeit import Timer

def benchmark(reps, setup, test):
    Timer(test, setup).timeit(reps)
    return Timer(test, setup).timeit(reps)

print(benchmark(1000, '''
def fib(n):
  return n if n < 2 else fib(n - 1) + fib(n - 2)
''', 'fib(20)'))
