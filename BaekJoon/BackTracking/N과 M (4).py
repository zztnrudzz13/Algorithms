import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

def dfs(index):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(index, N+1):
        arr.append(i)
        dfs(i)
        arr.pop()

dfs(1)