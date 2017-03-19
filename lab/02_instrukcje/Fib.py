import time
from Fib2 import fib3
from Fib_rek3 import fibonacciFast
import matplotlib.pylab as plt


def fib2(n):
    f1 = 0
    f2 = 1
    k = n - 2
    if n < 2:
        f2 = n
    else:
        while k >= 0:
            f2, f1, k = f1 + f2, f2, k-1
    return f2


def fib1(n):
    if n < 2:
        return n
    else:
        return fib1(n-1) + fib1(n-2)


# fibs = [fib1, fib2, fib3]
fibs = [fib3, fibonacciFast]

results = {f.__name__: [] for f in fibs}
print results

r_begin = 30000
r_end = 40000
r_range = range(r_begin, r_end, 100)

for n in r_range:
    print "n =", n,
    for f in fibs:
        start_time = time.clock()
        f(n)
        czas = time.clock() - start_time
        results[f.__name__].append(czas)
        print czas, "\t",
print results


# plt.plot(r_range, results["fib1"], linestyle='--', color='r')
plt.plot(r_range, results["fib2"], linestyle='-', color='g')
plt.plot(r_range, results["fib3"], linestyle='-', color='b')
plt.plot(r_range, results["fibonacciFast"], linestyle='-', color='r')
plt.show()
# for (x, y) in [(1, 2), (3, 4)]:
#     print y
