class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        arr = []
        visited = {num: False for num in nums}

        def dfs():
            if len(arr) == len(nums):
                tmp = arr[:]
                answer.append(tmp)
            for n in nums:
                if not visited[n]:
                    visited[n] = True
                    arr.append(n)
                    dfs()
                    arr.pop()
                    visited[n] = False

        dfs()
        return answer