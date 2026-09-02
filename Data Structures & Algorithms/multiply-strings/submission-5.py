class Solution:
    def plus(self, nums1: list[int], nums2: list[int])->list[int]:
        """
        nums1/2 are reversed order
        [8,7] + [0,6,2] -> 78 + 260
        8 + 0 + c
        7 + 6 + c
        0 + 2 + c
        output still the reversed order
        [1,2,3] -> 321
        """
        carry = 0
        sum_res = []
        l1 = len(nums1)
        l2 = len(nums2)

        for i in range(max(l1,l2)):
            # fill in zero
            if i >= l1:
                dig1 = 0
            else:
                dig1 = nums1[i]
            if i >= l2:
                dig2 = 0
            else:
                dig2 = nums2[i]

            _sum = dig1 + dig2 + carry
            sum_res.append(_sum%10)
            carry = _sum//10
        if carry != 0:
            sum_res.append(carry)

        return sum_res

    def multiply(self, num1: str, num2: str) -> str:
        nums1_lst = [ord(dig_str)-48 for dig_str in num1]
        nums2_lst = [ord(dig_str)-48 for dig_str in num2]


        len1 = len(nums1_lst)
        len2 = len(nums2_lst)

        long_num = nums1_lst if len1>= len2 else nums2_lst
        short_num = nums1_lst if len1<len2 else nums2_lst

        mult_matrix = [[] for _ in range(max(len1, len2))]

        for idx_long, dig_long in enumerate(long_num[::-1]):
            carry = 0
            mult_matrix[idx_long].extend([0]*idx_long)
            for idx_short, dig_short in enumerate(short_num[::-1]):
                _mult = dig_long * dig_short + carry
                mult_matrix[idx_long].append(_mult%10)
                carry = _mult//10
            if carry != 0:
                mult_matrix[idx_long].append(carry)

        final_sum = []

        for mult in mult_matrix:
            final_sum = self.plus(final_sum, mult)

        # trim the trailing zeros
        for i in range(len(final_sum)-1, 0, -1):
            if final_sum[i] == 0:
                final_sum.pop()
            else:
                break

        return "".join([chr(dig+48) for dig in final_sum[::-1]])
