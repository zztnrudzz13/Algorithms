import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
arr = []
visited = [False] * (N+1)

def dfs():
    if len(arr) == M:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return
        print(' '.join(map(str, arr)))
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs()
            arr.pop()
            visited[i] = False

dfs()