class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        long_sql_len = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                sql_len = 1
                target = nums[i] + 1
                while target in nums_set:
                    sql_len += 1
                    target += 1
                long_sql_len  = max(long_sql_len, sql_len)

            i += 1

        return long_sql_len
