class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        dic = {}
        nums.sort()
        for num in nums:
            dic.setdefault(num, 0)
            dic[num] += 1

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]
                dic[a] -= 1
                dic[b] -= 1
                c = 0 - (a + b)
                if c in dic and dic[c] > 0:
                    tmp = [a, b, c]
                    tmp.sort()
                    tmp = tuple(tmp)
                    answer.add(tmp)
                dic[a] += 1
                dic[b] += 1

        return answer