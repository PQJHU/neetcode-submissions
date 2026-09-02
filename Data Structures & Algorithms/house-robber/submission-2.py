class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_2, prev_1 = 0, 0

        for i in range(len(nums)):
            prev_2, prev_1 = prev_1, max(prev_1, nums[i] + prev_2)

        return prev_1
