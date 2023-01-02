import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))

L.sort()
result = 0

for i in range(len(L)):
    result += L[i] * (N - i)

print(result)
