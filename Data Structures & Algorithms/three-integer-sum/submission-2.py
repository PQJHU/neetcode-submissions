class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        three_sum_pairs = []
        for i, num in enumerate(nums):
            target = -num
            j = i + 1
            k = len(nums) -1
            while j < k:
                left_num, right_num = nums[j], nums[k]
                pair_sum = left_num + right_num
                if pair_sum == target:
                    if [num, left_num, right_num] not in three_sum_pairs:
                        three_sum_pairs.append([num, left_num, right_num])
                    j += 1
                    k -= 1
                elif pair_sum > target:
                    k -= 1
                else:
                    j += 1
        return three_sum_pairs
