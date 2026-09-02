class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_multi = [1 for _ in range(len(nums))]
        right_multi = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left_multi[i] = nums[i-1] * left_multi[i-1]

        for j in range(len(nums)-2, -1, -1):
            right_multi[j] = nums[j+1] * right_multi[j+1]

        res = [left_multi[k] * right_multi[k] for k in range(len(nums))]
        return res
