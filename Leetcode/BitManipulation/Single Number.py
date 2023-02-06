class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i, n in enumerate(nums):
            dic.setdefault(n, 0)
            dic[n] += 1
            if dic[n] == 2:
                del dic[n]

        answer = dic.keys()

        return list(answer)[0]