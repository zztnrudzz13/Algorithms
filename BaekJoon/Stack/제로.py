import sys
input = sys.stdin.readline

N = int(input())
L = []

for i in range(N):
    tmp = int(input())
    if tmp == 0:
        L.pop()
    else:
        L.append(tmp)

r = 0

for i in L:
    r += i

print(r)