def solution(arr):
    answer = [0, 0]

    def check(arr):
        f = arr[0][0]
        if len(arr) == 1:
            return [True, f]

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] != f:
                    return [False, 0]

        return [True, f]

    def divide(arr):
        result = check(arr)
        if result[0]:
            answer[result[1]] += 1
        else:
            N = len(arr)
            half = int(N / 2)
            left_up = [row[0:half] for row in arr[0:half]]
            left_down = [row[0:half] for row in arr[half:]]
            right_up = [row[half:] for row in arr[0:half]]
            right_down = [row[half:] for row in arr[half:]]
            divide(left_up)
            divide(left_down)
            divide(right_up)
            divide(right_down)

    divide(arr)

    return answer