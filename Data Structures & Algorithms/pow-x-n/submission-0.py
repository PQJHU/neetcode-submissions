class Solution:
    def myPow(self, x: float, n: int) -> float:
            
        def pow_pos(x:float, n:int)->float:
            if n == 0:
                return 1
            if n == 1:
                return x
            if n%2 == 0:
                return pow_pos(x*x, n//2)
            else:
                return x* pow_pos(x*x, n//2)
            
        if n < 0:
            res = pow_pos(x, -n)
            return 1/res
        else:
            return pow_pos(x, n)