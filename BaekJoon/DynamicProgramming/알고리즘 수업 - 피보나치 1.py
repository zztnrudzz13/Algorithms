import sys
input = sys.stdin.readline

N = int(input())
L = [0, 0]
f = []

def fib(n):
    if n == 1 or n == 2:
        L[0] += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)


f.append(0)
f.append(1)
f.append(1)


def fibonacci(n):
    for i in range(3, n+1):
        L[1] += 1
        f.append(f[i-1] + f[i-2])
    return f[n]


print(fibonacci(N), L[1])