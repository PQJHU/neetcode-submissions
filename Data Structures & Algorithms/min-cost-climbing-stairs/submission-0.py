class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n =len(cost)
        acc_min_cost = [0] * n
        acc_min_cost[0] = cost[0]
        acc_min_cost[1] = cost[1]

        for i in range(2,n):
            acc_min_cost[i] = cost[i] + min(acc_min_cost[i-1], acc_min_cost[i-2])

        return min(acc_min_cost[-2], acc_min_cost[-1])
        