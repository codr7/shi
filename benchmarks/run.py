from timeit import Timer

def benchmark(reps, setup, test):
    Timer(test, setup).timeit(reps)
    return Timer(test, setup).timeit(reps)

print('fact', benchmark(500000, '''
def fact(acc, n):
  return acc if n == 1 else fact(n * acc, n - 1)
''',
'fact(1, 15)'))

print('fib', benchmark(500, '''
def fib(n):
  return n if n < 2 else fib(n - 1) + fib(n - 2)
''', 'fib(20)'))
