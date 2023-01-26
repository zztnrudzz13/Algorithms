import sys
import math
input = sys.stdin.readline
N = int(input())

nums = list(map(int, input().split()))
ex = list(map(int, input().split()))
result = nums[0]
arr = []
min_num = math.inf
max_num = -math.inf
count = 0
e = ''

dic = {
    0: '+',
    1: '-',
    2: '*',
    3: '/'
}

def dfs():
    global e, min_num, max_num, count, result
    if e != '':
        if result < 0 and nums[count] > 0 and e == '/':
            result = -int(-result / nums[count])
        else:
            result = int(eval(str(result)+e+str(nums[count])))
    if count == len(nums)-1:
        max_num = max_num if max_num >= result else result
        min_num = min_num if min_num <= result else result
    for i in range(len(ex)):
        if ex[i] > 0:
            ex[i] -= 1
            e = dic[i]
            count += 1
            arr.append(result)
            arr.append(e)
            dfs()
            count -= 1
            ex[i] += 1
            arr.pop()
            result = arr.pop()

dfs()

print(max_num)
print(min_num)