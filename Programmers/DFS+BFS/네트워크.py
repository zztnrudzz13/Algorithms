from collections import deque

def solution(n, computers):
    answer = 0
    q = deque()
    visited = [False] * n

    def bfs(v):
        visited[v] = True
        q.append(v)
        while len(q) != 0:
            u = q.popleft()
            for g in range(len(computers[u])):
                if computers[u][g] == 1 and not visited[g]:
                    visited[g] = True
                    q.append(g)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer