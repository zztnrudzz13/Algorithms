import sys
input = sys.stdin.readline

N = int(input())
result = 0

def plus(n):
    tmp = n
    n = str(n)
    for i in n:
        tmp += int(i)

    return tmp

for i in range(1, N):
    if plus(i) == N:
        result = i
        break

print(result)