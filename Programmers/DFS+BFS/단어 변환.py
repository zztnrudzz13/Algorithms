from collections import deque


def solution(begin, target, words):
    answer = []
    q = deque()
    count = 0
    if target not in words:
        return 0

    words.append(begin)
    dic = {word: [] for word in words}
    visited = {word: False for word in words}

    for word in words:
        for comparison in words:
            count = 0
            if word == comparison:
                dic[word].append(comparison)
            else:
                for i in range(len(word)):
                    if word[i] != comparison[i]:
                        count += 1
                if count == 1:
                    dic[word].append(comparison)

    def bfs(v, count):
        visited[v] = True
        q.append((v, 0))
        while len(q) != 0:
            u, c = q.popleft()
            for g in dic[u]:
                if not visited[g]:
                    if g == target:
                        answer.append(c + 1)
                    visited[g] = True
                    q.append((g, c + 1))

    bfs(begin, count)

    if len(answer) == 0:
        return 0

    return min(answer)