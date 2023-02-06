class Solution:
    sums = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        arr = []
        visited = [False] * len(candidates)

        if sum(candidates) < target:
            return []

        def backtracking(n):
            if self.sums == target:
                tmp = arr[:]
                answer.append(tmp)

            prev = -1
            for i in range(n + 1, len(candidates)):
                if prev == candidates[i]:
                    continue
                if self.sums < target:
                    arr.append(candidates[i])
                    self.sums += candidates[i]
                    backtracking(i)
                    minus = arr.pop()
                    self.sums -= minus
                    prev = candidates[i]

        backtracking(-1)

        answer = [list(t) for t in answer]

        return answer