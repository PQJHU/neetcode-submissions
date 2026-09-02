from functools import lru_cache


class Solution:

    @lru_cache(maxsize=128)
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        elif n==1:
            return 1
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)
