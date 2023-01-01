N = int(input())
L = list(map(int, input().split()))
dic = {}

for num in L:
    try:
        dic[num].append(num)
    except:
        dic[num] = [num]

key = list(dic.keys())
key.sort()

for i in range(len(key)):
    dic[key[i]].append(i)

for num in L:
    print(dic[num][-1], end=' ')

