class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        n = len(digits)
        for i in range(n):
            integer += digits[i] * 10 ** (n-i-1)
        plus_one = integer + 1
        plus_one_digits = []
        while plus_one != 0:
            plus_one_digits.append(plus_one%10)
            plus_one = plus_one // 10
        return plus_one_digits[-1::-1]
        