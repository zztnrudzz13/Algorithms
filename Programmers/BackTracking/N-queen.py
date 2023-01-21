def solution(n):
    answer = [0]
    arr = [i for i in range(n)]
    visited = [False for i in range(n)]
    s = []

    def isValid(s, g):
        g_x = len(s)
        g_y = g
        for i in range(len(s)):
            x = i
            y = s[i]
            if abs(g_y - y) == abs(g_x - x):
                return False
        return True

    def dfs(v):
        s.append(v)
        visited[v] = True
        if len(s) == n:
            answer[0] += 1
        for g in arr:
            if not visited[g] and isValid(s, g):
                dfs(g)
                s.pop()
                visited[g] = False

    for i in range(n):
        visited[i] = True
        s = []
        dfs(i)
        visited[i] = False

    return answer[0]