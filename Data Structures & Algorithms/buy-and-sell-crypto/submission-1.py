class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        left, right = 0, 1
        while right < n:
            profit = prices[right] - prices[left]
            if profit <= 0:
                left, right = right, right + 1
            else:
                max_profit = max(profit, max_profit)
                right += 1

        return max_profit
