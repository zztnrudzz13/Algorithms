import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
visited = [False] * (N+1)

def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        if visited[i]:  # 이미 방문한 노드는 건너뛰기
            continue
        visited[i] = True  # 방문 안 한 노드라면 True로 바꾸고 arr에 추가
        arr.append(i)
        dfs()  # dfs 다시 호출했을 떄 첫 if 문에 걸리고 return 되면,
        arr.pop()  # arr에서 마지막 원소 다시 꺼내고
        visited[i] = False  # False 상태로 바꿔주기

dfs()
