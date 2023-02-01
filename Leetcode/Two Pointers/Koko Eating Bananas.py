import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        start = 1
        end = piles[len(piles) - 1]
        answer = end

        def check(num):
            tmp = 0
            for pile in piles:
                tmp += int(math.ceil(pile / num))
                if tmp > h:
                    return h + 1
            return tmp

        while start <= end:
            if end - start == 1:
                if check(start) <= h:
                    answer = min(start, answer)
                if check(end) <= h:
                    answer = min(end, answer)
                break

            mid = (start + end) // 2
            tmp = check(mid)
            if tmp > h:
                start = mid
            elif tmp <= h:
                answer = min(mid, answer)
                end = mid
        return answer