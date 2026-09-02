class Solution:

    def digits(self, n: int)-> list[int]:
        res =  []
        while n > 0:
            res.append(n%10)
            n = n//10
        return res

    def isHappy(self, n: int) -> bool:
        sums = set()
        while n != 1:
            digs = self.digits(n)
            n = sum(dig**2 for dig in digs)
            if n in sums:
                return False
            sums.add(n)
        return True
        