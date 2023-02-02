class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])

        start = 0
        end = len(nums) - 1

        while end - start != 1:
            print(start, end)
            mid = (start + end) // 2
            print(nums[start], nums[mid], nums[end])
            arr = [start, mid, end]
            if nums[start] < nums[mid] < nums[end]:
                end = mid
            elif nums[start] < nums[end] < nums[mid]:
                start = mid
            elif nums[mid] < nums[end] < nums[start]:
                # 놓친 지점
                end = mid
            elif nums[mid] < nums[start] < nums[end]:
                end = mid
            elif nums[end] < nums[start] < nums[mid]:
                start = mid
            elif nums[end] < nums[mid] < nums[start]:
                start = mid

        return min(nums[start], nums[end])