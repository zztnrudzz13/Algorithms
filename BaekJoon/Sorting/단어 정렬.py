N = int(input())
L = []

for i in range(N):
    L.append(input())

S = list(set(L))
S.sort(key=lambda x: (len(x), x))

for word in S:
    print(word)