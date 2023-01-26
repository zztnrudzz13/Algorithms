import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

N = int(input())
arr = []
visited = [False] * N
answer = 0




def dfs(index):
    global answer
    if N == 1:
        answer += 1
        return
    if len(arr) > 1:
        [x1, y1] = arr[-1]
        for a in arr[:-1]:
            [x2, y2] = a
            if abs(x1 - x2) == abs(y1 - y2):
                return
        if len(arr) == N:
            answer += 1
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append([index, i])
            index += 1
            dfs(index)
            arr.pop()
            index -= 1
            visited[i] = False


dfs(0)

print(answer)