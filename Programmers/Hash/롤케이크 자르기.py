from collections import Counter

def solution(topping):
    answer = 0
    c = Counter(topping)
    dic = {}

    for num in topping:
        c[num] -= 1
        if c[num] == 0:
            del c[num]
        try:
            dic[num] += 1
        except:
            dic[num] = 1

        if len(dic) == len(c):
            answer += 1

    return answer
