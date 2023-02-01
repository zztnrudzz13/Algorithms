import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        reverse_nums = [-i for i in nums]
        heapq.heapify(reverse_nums)

        answer = 0
        while k > 0:
            answer = heapq.heappop(reverse_nums)
            k -= 1

        return -answer