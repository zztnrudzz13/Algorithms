class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m * n - 1

        def makePoint(num):
            i = max(int(num // n), 0)
            j = max(num - (n * i), 0)

            return [i, j]

        if m == 1 and n == 1:
            return True if matrix[0][0] == target else False

        while start <= end:
            mid = int((start + end) // 2)
            [i, j] = makePoint(mid)
            if end - start == 1:
                [ei, ej] = makePoint(end)
                [si, sj] = makePoint(start)
                if matrix[ei][ej] == target or matrix[si][sj] == target:
                    return True
                else:
                    return False
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                end = mid
            elif matrix[i][j] < target:
                start = mid

        return False