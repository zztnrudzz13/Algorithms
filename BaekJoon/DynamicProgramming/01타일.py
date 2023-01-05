import sys
input = sys.stdin.readline

L = []

L.append(0)
L.append(1)
L.append(2)

N = int(input())
def tile(n):
    for i in range(3, N+1):
        L.append((L[i-1] + L[i-2]) % 15746)

tile(N)

print(L[N])