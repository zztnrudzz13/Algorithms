import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_d = [False] * (n+1)
visited_b = [False] * (n+1)

q = deque()
result_d = []
result_b = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(arr) for arr in graph]


def dfs(v):
    visited_d[v] = True
    result_d.append(v)
    for g in graph[v]:
        if not visited_d[g]:
            dfs(g)

def bfs(v):
    q.append(v)
    visited_b[v] = True
    while len(q) != 0:
        u = q.popleft()
        result_b.append(u)
        for g in graph[u]:
            if not visited_b[g]:
                visited_b[g] = True
                q.append(g)


dfs(r)
bfs(r)

for i in range(len(result_d)):
    print(result_d[i], end=' ')

print()
for i in range(len(result_b)):
    print(result_b[i], end=' ')

