import sys
input = sys.stdin.readline

N = int(input())
L = []

for i in range(N):
    L.append(input())

def check(s):
    S = []
    for p in s:
        if p == '(':
            S.append('(')
        if p == ')':
            if len(S) == 0 or S[-1] != '(':
                return False
            else:
                S.pop()
    return True if len(S) == 0 else False

for string in L:
    if check(string):
        print('YES')
    else:
        print('NO')