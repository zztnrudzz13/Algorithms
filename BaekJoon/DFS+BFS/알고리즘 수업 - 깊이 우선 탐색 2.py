import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(arr, reverse=True) for arr in graph]

def dfs(v):
    global count
    visited[v] = count
    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            dfs(g)


dfs(r)

for i in range(1, len(visited)):
    print(visited[i])