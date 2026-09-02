class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi_res = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                multi_res *= num

        res = []
        if zero_count > 1:
            return [0]*len(nums)

        for num in nums:

            if zero_count == 1:
                if num == 0:
                    res.append(multi_res)
                else:
                    res.append(0)
            else:
                res.append(int(multi_res/num))
        return res
