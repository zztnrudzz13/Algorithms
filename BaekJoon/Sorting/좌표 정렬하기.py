N = int(input())
L = []

for i in range(N):
    x, y = input().split()
    L.append([int(x), int(y)])

L.sort(key = lambda x: (x[0], x[1]))

for arr in L:
    print(arr[0], arr[1])