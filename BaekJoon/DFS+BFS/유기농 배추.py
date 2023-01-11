import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

T = int(input())
case = [[] for _ in range(T)]
result = [0] * T

for i in range(T):
    M, N, K = map(int, input().split())
    case[i] = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        case[i][y][x] = 1

def dfs(x, y, arr):
    arr[x][y] = 0
    if x+1 < len(arr) and arr[x+1][y] == 1:
        dfs(x+1, y, arr)
    if x-1 >= 0 and arr[x-1][y] == 1:
        dfs(x-1, y, arr)
    if y+1 < len(arr[0]) and arr[x][y+1] == 1:
        dfs(x, y+1, arr)
    if y-1 >= 0 and arr[x][y-1] == 1:
        dfs(x, y-1, arr)


for i in range(T):
    for x in range(len(case[i])):
        for y in range(len(case[i][0])):
            if case[i][x][y] == 1:
                dfs(x, y, case[i])
                result[i] += 1


for num in result:
    print(num)
