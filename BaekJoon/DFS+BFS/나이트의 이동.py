import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
result = []


def bfs(x, y, n):
    q = deque()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    q.append([x, y])

    while len(q) != 0:
        [x, y] = q.popleft()

        if x == ex and y == ey:
            return visited[x][y]-1

        for dx, dy in [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

for _ in range(N):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    result.append(bfs(sx, sy, n))

for num in result:
    print(num)

