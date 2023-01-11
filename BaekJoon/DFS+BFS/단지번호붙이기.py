import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
graph = []
result = []
count = 0

for _ in range(N):
    tmp = input()[:-1]
    arr = []
    for num in tmp:
        arr.append(int(num))
    graph.append(arr)

def dfs(x, y, arr):
    arr[x][y] = 0
    result[count] += 1
    if x+1 < N and arr[x+1][y] == 1:
        dfs(x+1, y, arr)
    if x-1 >= 0 and arr[x-1][y] == 1:
        dfs(x-1, y, arr)
    if y+1 < N and arr[x][y+1] == 1:
        dfs(x, y+1, arr)
    if y-1 >= 0 and arr[x][y-1] == 1:
        dfs(x, y-1, arr)

for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            result.append(0)
            dfs(x, y, graph)
            count += 1

print(len(result))
result.sort()
for num in result:
    print(num)