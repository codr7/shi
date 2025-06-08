from timeit import Timer

def benchmark(reps, setup, test):
    Timer(test, setup).timeit(reps)
    return Timer(test, setup).timeit(reps)

print('fact', benchmark(500000, '''
def fact(acc, n):
  return acc if n == 1 else fact(n * acc, n - 1)
''',
'fact(1, 15)'))

print('fib1', benchmark(500, '''
def fib(n):
  return n if n < 2 else fib(n - 1) + fib(n - 2)
''', 'fib(20)'))

print('fib2', benchmark(500000, '''
def fib(n, a, b):
  return a if n == 0 else b if n == 1 else fib(n-1, b, a+b)
''',
'fib(20, 0, 1)'))
