class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] + ([1] * (len(nums) - 1))
        suffix = ([1] * (len(nums) - 1)) + [nums[-1]]
        answer = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        answer[0] = suffix[1]

        for i in range(1, len(nums)):
            if i == len(nums) - 1:
                answer[i] = prefix[i - 1]
            else:
                answer[i] = suffix[i + 1] * prefix[i - 1]

        return answer