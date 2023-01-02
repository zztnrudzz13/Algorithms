import sys
input = sys.stdin.readline

N = int(input())
L = []
S = []
result = []
count = 0

for i in range(N):
    L.append(int(input()))

L.reverse()
tmp = [i for i in range(1, N+1)]
tmp.reverse()

while len(L) > 0:
    if len(tmp) == 0 and L[-1] != S[-1]:
        break
    if len(S) != 0:
        if L[-1] == S[-1]:
            S.pop()
            L.pop()
            result.append('-')
            count += 1
        else:
            num = tmp.pop()
            S.append(num)
            result.append('+')
    elif len(S) == 0:
        num = tmp.pop()
        S.append(num)
        result.append('+')

if count == N:
    for i in result:
        print(i)
else:
    print('NO')
