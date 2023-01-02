import sys

N = int(input())
L = [['*' for i in range(N)] for j in range(N)]

def delete(arr):
    length = int(len(arr) / 3)
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            arr[i][j] = ' '

def recursion(arr, num):
    # delete(arr)
    for i in range(0, len(arr), 3**num):
        print(i, i+3)
        print(L[i])
        for j in range(0, len(L[i]), 3**num):
            tmp = [row[j:j+3] for row in L[i:i+3]]
            delete(tmp)
            print(tmp)


    # if 3 ** (num + 1)

recursion(L, 1)

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end='')
    print()