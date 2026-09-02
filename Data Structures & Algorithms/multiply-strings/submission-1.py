class Solution:
    def str_to_int(self,s:str)->int:
        n = len(s)
        res = 0
        for i in range(n):
            digit = ord(s[i]) - 48
            res = res + digit * 10 ** (n-i-1)
        return res

    def int_to_str(self, i:int)->str:
        str_lst = []

        def recursive_way(i:int)-> int:
            if i == 0:
                return
            str_lst.append(chr(i%10 + 48))
            return recursive_way(i//10)


        def iterative_way(i:int):
            while i >0 or not str_lst:
                str_lst.append(chr(i%10 + 48))
                i = i//10

        iterative_way(i)

        return "".join(str_lst[::-1])

    def multiply(self, num1: str, num2: str) -> str:
        multi = self.str_to_int(num1) * self.str_to_int(num2)
        return self.int_to_str(multi)
