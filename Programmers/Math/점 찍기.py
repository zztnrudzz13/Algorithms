import math

def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k):
        tmp = d ** 2 - i ** 2
        sqrt = tmp ** 0.5
        answer += math.ceil((int(sqrt) + 1) / k)

    return answer