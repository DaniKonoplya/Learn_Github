import time


def method1():
    l = []
    for n in range(10000):
        l = l + [n]
    return l


def method2():
    l = []
    for n in range(10000):
        l.append(n)
    return l


def method3():
    l = [n for n in range(10000)]
    return l


def method4():
    l = list(range(10000))
    return l


tic = time.perf_counter()
method1()
toc = time.perf_counter()
print(f" Difference1 is  {toc - tic} seconds")

tic = time.perf_counter()
method2()
toc = time.perf_counter()
print(f" Difference2 is  {toc - tic} seconds")

tic = time.perf_counter()
method3()
toc = time.perf_counter()
print(f" Difference3 is  {toc - tic} seconds")


tic = time.perf_counter()
method4()
toc = time.perf_counter()
print(f" Difference4 is  {toc - tic} seconds")
