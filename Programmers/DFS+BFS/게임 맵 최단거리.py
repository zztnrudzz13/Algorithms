from collections import deque


def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]

    ex = n - 1
    ey = m - 1

    def bfs(x, y):
        q = deque()
        q.append([x, y])
        visited[x][y] = 1

        while len(q) != 0:
            [x, y] = q.popleft()

            if x == ex and y == ey:
                answer.append(visited[x][y])

            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

        if visited[ex][ey] == 0:
            answer.append(-1)

    bfs(0, 0)
    return max(answer)