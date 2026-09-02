class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n):
            for j in range(i+1, n):
                max_profit=  max(prices[j] - prices[i], max_profit)
        return max_profit
        