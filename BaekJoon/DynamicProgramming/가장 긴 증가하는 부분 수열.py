import sys

input = sys.stdin.readline
N = int(input())
L = [0] + list(map(int, input().split()))
result = [0] + [0 for i in range(N)]

result[1] = 1

for i in range(2, N+1):
    num = L[i]
    max_num = 0
    for j in range(0, i):
        if L[j] < num and result[j] >= max_num:
            max_num = result[j]
    result[i] = 1 if max_num == 0 else max_num + 1

print(max(result))

