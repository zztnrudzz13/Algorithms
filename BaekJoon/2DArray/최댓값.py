import sys
input =  sys.stdin.readline
L = []
max_num = -1
index = [-1, -1]

for i in range(9):
    L.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if L[i][j] == 99:
            max_num = 99
            index = [i, j]
            break
        if L[i][j] > max_num:
            max_num = L[i][j]
            index = [i, j]
    if max == 99:
        break

print(max_num)
print(index[0]+1, index[1]+1)