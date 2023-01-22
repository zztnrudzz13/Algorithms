def solution(line):
    answer = []
    s = set()

    def find_point(arr1, arr2):
        [A, B, E] = arr1
        [C, D, F] = arr2
        x_up = (B * F) - (E * D)
        y_up = (E * C) - (A * F)
        down = (A * D) - (B * C)

        return [x_up / down, y_up / down]

    for i in range(len(line)):
        for j in range(i, len(line)):
            [A, B, E] = line[i]
            [C, D, F] = line[j]
            if (A * D) - (B * C) != 0:
                [x, y] = find_point(line[i], line[j])
                if float.is_integer(x) and float.is_integer(y):
                    s.add((int(x), int(y)))

    points = list(s)
    points.sort(key=lambda x: x[0])
    min_x, max_x = points[0][0], points[-1][0]
    points.sort(key=lambda x: x[1])
    min_y, max_y = points[0][1], points[-1][1]

    d_x = max_x - min_x
    d_y = max_y - min_y
    arr = [['.'] * (d_x + 1) for _ in range(d_y + 1)]

    def find_x(x):
        return x - min_x

    def find_y(y):
        return max_y - y

    for x, y in points:
        x = find_x(x)
        y = find_y(y)
        arr[y][x] = '*'

    for l in arr:
        answer.append(''.join(l))

    return answer