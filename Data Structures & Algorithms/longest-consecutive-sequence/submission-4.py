class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        long_seq_len = 0
        i = 0
        sql_len = 1
        
        if len(nums_sorted) == 1:
            return 1
        
        while i < len(nums)-1:
            if nums_sorted[i+1] == nums_sorted[i]:
                i+=1
            elif nums_sorted[i+1] - nums_sorted[i] ==1:
                sql_len += 1
                i += 1
            else:
                sql_len = 1
                i += 1

            long_seq_len = max(long_seq_len, sql_len)
        return long_seq_len
