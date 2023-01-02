import sys
input = sys.stdin.readline

N, M = input().split()
N = int(N)
L = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = L[i] + L[j] + L[k]
            if result < tmp <= int(M):
                result = tmp

print(result)