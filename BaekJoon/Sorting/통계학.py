import sys
input = sys.stdin.readline

N = int(input())
plus = 0
L = []
max_num = 0
max_list = []
dic = {}

for i in range(N):
    tmp = int(input())
    plus += tmp
    L.append(tmp)
    try:
        dic[tmp] += 1
    except:
        dic[tmp] = 1
L.sort()
mean = round(plus / N)
middle = L[int((N-1)/2)]
r = L[-1] - L[0]

for i in dic:
    if dic[i] > max_num:
        max_num = dic[i]
        max_list = [i]
    elif dic[i] == max_num:
        max_list.append(i)

max_list.sort()
frequency = max_list[0] if len(max_list) == 1 else max_list[1]

print(mean)
print(middle)
print(frequency)
print(r)

