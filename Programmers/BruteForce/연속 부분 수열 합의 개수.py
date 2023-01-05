def solution(elements):
    answer = []

    for i in range(len(elements) - 1):
        arr = elements + elements[:i]
        for j in range(len(arr)):
            if i + j + 1 <= len(arr):
                tmp = arr[j:i + j + 1]
                answer.append(sum(tmp))

    return len(set(answer)) + 1