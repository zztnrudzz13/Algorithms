import math

def solution(N, road, K):
    answer = 0
    neighbor = [[] for _ in range(N + 1)]
    maps = [[math.inf] * (N + 1) for _ in range(N + 1)]

    visited = [True, False] + [False] * (N - 1)
    distance = [math.inf, 0] + [math.inf] * (N - 1)

    for arr in road:
        [s, e, d] = arr
        if e not in neighbor[s]:
            neighbor[s].append(e)
        if s not in neighbor[e]:
            neighbor[e].append(s)
        maps[s][e] = maps[s][e] if maps[s][e] < d else d
        maps[e][s] = maps[e][s] if maps[e][s] < d else d

    def dijkstra(v):
        visited[v] = True
        distance[v] = 0
        for e in neighbor[v]:
            distance[e] = min(distance[e], maps[v][e])
        while False in visited:
            u = 0
            tmp = math.inf
            for i in range(1, len(distance)):
                if not visited[i] and tmp > distance[i]:
                    u = i
                    tmp = distance[i]
            visited[u] = True
            for e in neighbor[u]:
                distance[e] = min(distance[e], distance[u] + maps[u][e])

    dijkstra(1)

    for num in distance:
        if num <= K:
            answer += 1

    return answer