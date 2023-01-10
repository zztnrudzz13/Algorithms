import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
count = 1

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(arr) for arr in graph]


def dfs(v):
    global count
    visited[v] = count
    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            dfs(g)


dfs(R)

for i in range(1, len(visited)):
    print(visited[i])
