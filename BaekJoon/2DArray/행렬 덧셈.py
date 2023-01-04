import sys
input = sys.stdin.readline

N, M = input()[:-1].split()
A = []
B = []
result = [[-1 for i in range(int(M))] for j in range(int(N))]

for i in range(int(N)):
    tmp = list(map(int, input().split()))
    A.append(tmp)

for i in range(int(N)):
    tmp = list(map(int, input().split()))
    B.append(tmp)

for i in range(int(N)):
    for j in range(int(M)):
        result[i][j] = A[i][j] + B[i][j]

for i in range(int(N)):
    for j in range(int(M)):
        print(result[i][j], end=' ')
    print()
