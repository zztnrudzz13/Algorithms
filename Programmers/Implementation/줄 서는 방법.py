def solution(n, k):
    answer = []
    arr = [i + 1 for i in range(n)]

    def factorial(n):
        tmp = 1
        for i in range(1, n + 1):
            tmp *= i
        return tmp

    for i in range(n - 1):
        fac = factorial(n - i - 1)
        a = int(k // fac)
        k = int(k % fac)
        if k == 0:
            a -= 1
            k += fac
        answer.append(arr[a])
        arr = arr[:a] + arr[a + 1:]
    left = set(arr) - set(answer)
    return answer + list(left)