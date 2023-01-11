import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
result = []

ex, ey = N-1, M-1

for _ in range(N):
    tmp = []
    arr = input()[:-1]
    for num in arr:
        tmp.append(int(num))
    graph.append(tmp)

visited = [[0] * M for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while len(q) != 0:
        [x, y] = q.popleft()
        if x == ex and y == ey:
            result.append(visited[x][y])

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[x][y] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

bfs(0, 0)
print(max(result))
