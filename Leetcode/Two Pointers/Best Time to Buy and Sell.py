class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        lowest = prices[0] # lowest가 왼쪽 포인터
        for price in prices:  # price가 오른쪽 포인터
            if price < lowest:
                lowest = price
            answer = max(answer, price-lowest)
        return answer