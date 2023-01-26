import sys
import math
input = sys.stdin.readline

answer = math.inf
N = int(input())
arr = []
visited = [False] * N
stats = [list(map(int, input().split())) for _ in range(N)]

def dfs(index):
    global answer
    if len(arr) == int(N/2):
        print(arr)
        s1 = 0
        s2 = 0
        tmp = []
        for i in range(len(visited)):
            if not visited[i]:
                tmp.append(i)
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                s1 += stats[arr[i]][arr[j]] + stats[arr[j]][arr[i]]
                s2 += stats[tmp[i]][tmp[j]] + stats[tmp[j]][tmp[i]]
        answer = answer if answer <= abs(s1-s2) else abs(s1-s2)
    for i in range(index+1, N):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(i)
            arr.pop()
            visited[i] = False



dfs(0)
print(answer)
