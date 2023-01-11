import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
q = deque()
count = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(arr, reverse=True) for arr in graph]

def bfs(v):
    global count
    visited[v] = count
    q.append(v)
    while len(q) != 0:
        u = q.popleft()
        for g in graph[u]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                q.append(g)

bfs(r)

for i in range(1, len(visited)):
    print(visited[i])