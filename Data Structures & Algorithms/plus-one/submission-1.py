class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        plus_one_digits = []
        for digit in digits[-1::-1]:
            _sum = digit + carry
            carry = _sum//10
            plus_one_digits.append(_sum%10)
        if carry != 0:
            plus_one_digits.append(carry)
        return plus_one_digits[-1::-1]
