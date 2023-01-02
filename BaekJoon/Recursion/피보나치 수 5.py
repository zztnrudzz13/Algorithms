import sys
input = sys.stdin.readline

N = int(input())

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return fib(n-1) + fib(n-2)

print(fib(N))