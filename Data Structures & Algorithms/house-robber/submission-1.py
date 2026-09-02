class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        val = [0]* len(nums)
        val[0] = nums[0]
        val[1] = nums[1]
        for i in range(2, len(nums)):  # when i =2, val[i-3] will refer to 0
            num = nums[i]
            val[i] = num + max(val[i-2], val[i-3])

        return max(val[n-1], val[n-2])
        