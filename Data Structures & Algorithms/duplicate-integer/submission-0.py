class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_map = dict()
        for num in nums:
            if num in check_map:
                return True
            else:
                check_map[num] = True
        return False

        