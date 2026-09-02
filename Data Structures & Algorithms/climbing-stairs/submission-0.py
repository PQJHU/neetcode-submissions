class Solution:
    def climbStairs(self, n: int) -> int:
        res_array = [0 for _ in range(n+1)]
        for i in range(n+1):
            if i == 0:
                res_array[0] = 1
            elif i == 1:
                res_array[1] = 1
            else:
                res_array[i] = res_array[i-1] + res_array[i-2]

        return res_array[-1]

        