import sys
import math
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
visited = [math.inf] * 200001

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while len(q) != 0:
        u = q.popleft()
        if u == K:
            return visited[u]
        for i in [u - 1, u + 1, 2 * u]:
            if 0 <= i < 200001 and visited[i] > visited[u] + 1:
                visited[i] = visited[u] + 1
                q.append(i)


answer = bfs(N)
print(answer - 1)
