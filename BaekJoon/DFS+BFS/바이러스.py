import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
q = deque()
count = 1

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(v):
    global count
    visited[v] = True
    q.append(v)
    while len(q) != 0:
        u = q.popleft()
        for g in graph[u]:
            if not visited[g]:
                count += 1
                visited[g] = True
                q.append(g)

bfs(1)
print(count - 1)

