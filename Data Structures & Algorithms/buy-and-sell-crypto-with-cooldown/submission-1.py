class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def dfs(i: int, can_buy:bool)->int:
            # print(i, can_buy)
            if i >= n:
                return 0

            if (i, can_buy) in dp:
                return dp[(i, can_buy)]

            if can_buy:
                buy = dfs(i+1, not can_buy) - prices[i]
                cooldown = dfs(i+1, can_buy)
                dp[(i, can_buy)] = max(buy, cooldown)
                print(i, 'buy' if buy > cooldown else 'cooldown')
            else:
                sell = dfs(i+2, can_buy=True) + prices[i]
                cooldown = dfs(i+1, can_buy=can_buy)
                dp[(i, can_buy)] = max(sell, cooldown)
                print(i, 'sell' if sell > cooldown else 'cooldown')

            return dp[(i, can_buy)]

        return dfs(0, True)
  