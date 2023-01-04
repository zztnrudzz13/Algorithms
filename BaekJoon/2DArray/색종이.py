import sys
input = sys.stdin.readline

N = int(input())
L = [[0 for i in range(99)] for j in range(99)]
result = 0

for i in range(N):
    arr = list(map(int, input().split()))
    x, y = arr[0]-1, arr[1]-1
    for j in range(x, x+10):
        for k in range(y, y+10):
            L[j][k] = 1

for i in range(99):
    for j in range(99):
        if L[i][j] == 1:
            result += 1

print(result)