class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        lowest = prices[0]
        profit = 0
        right = 1
        while (right < len(prices)):
            if (prices[right]-lowest > profit):
                profit = prices[right] - lowest
            elif prices[left] > prices[right]:
                left = right
                lowest = prices[left]
            right += 1
        if profit < 0:
            return 0
        return profit