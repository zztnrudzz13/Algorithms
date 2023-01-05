import sys
input = sys.stdin.readline

L = [[[-1 for i in range(21)] for j in range(21)] for k in range(21)]
result = []

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                L[i][j][k] = 1


def w(a, b, c):
    if 0 < a <= 20 and 0 < b <= 20 and 0 < c <= 20:
        if L[a][b][c] != -1:
            return L[a][b][c]
        elif a < b < c:
            L[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return L[a][b][c]
        else:
            L[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
            return L[a][b][c]
    elif a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)



while True:
    tmp = list(map(int, input().split()))
    a, b, c = tmp[0], tmp[1], tmp[2]
    if a == -1 and b == -1 and c == -1:
        break
    else:
        result.append([a, b, c, w(a,b,c)])

for arr in result:
    print('w(' + str(arr[0]) + ', ' + str(arr[1]) + ', ' + str(arr[2]) + ') = ' + str(arr[3]))
