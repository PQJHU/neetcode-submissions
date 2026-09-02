class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_space = dict()
        for j in range(len(nums)):
            search_num = target - nums[j]
            if search_num in search_space:
                return [search_space[search_num], j]
            else:
                search_space[nums[j]] = j
        return []
        