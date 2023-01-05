import sys
input = sys.stdin.readline

N = int(input())
L = [[0 for i in range(10)] for j in range(N+1)]

L[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            L[i][j] = L[i-1][1]
        elif 1 <= j <= 8:
            L[i][j] = L[i-1][j-1] + L[i-1][j+1]
        elif j == 9:
            L[i][j] = L[i-1][8]

print(sum(L[-1]) % 1000000000)