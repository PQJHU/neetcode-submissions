class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        three_sum_pairs = []
        for i, num in enumerate(nums):
            if i >0 and nums[i] == nums[i-1]:
                continue
            target = -num
            j = i + 1
            k = len(nums) -1
            while j < k:
                left_num, right_num = nums[j], nums[k]
                pair_sum = left_num + right_num
                if pair_sum == target:
                    three_sum_pairs.append([num, left_num, right_num])
                    j += 1
                    k -= 1
                    while j <k and nums[j] == nums[j-1]:
                        j+=1
                    while j< k and nums[k] == nums[k+1]:
                        k-=1
                elif pair_sum > target:
                    k -= 1
                else:
                    j += 1
        return three_sum_pairs
