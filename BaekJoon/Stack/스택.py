import sys
input = sys.stdin.readline
S = []
N = int(input())
L = []

for i in range(N):
    tmp = input()[:-1].split(' ')
    L.append(tmp)

for arr in L:
    tmp = arr[0]
    if tmp == 'push':
        S.append(arr[1])
    elif tmp == 'pop':
        if len(S) != 0:
            n = S.pop()
            print(n)
        else:
            print(-1)
    elif tmp == 'size':
        print(len(S))
    elif tmp == 'empty':
        result = 1 if len(S) == 0 else 0
        print(result)
    elif tmp == 'top':
        if len(S) != 0:
            print(S[-1])
        else:
            print(-1)