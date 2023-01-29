from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        values = c.values()
        for num in values:
            if num > 1:
                return True

        return False
