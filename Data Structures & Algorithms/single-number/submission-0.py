class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_mapping = dict()
        for num in nums:
            num_mapping[num] = num_mapping.get(num, 0) + 1
            if num_mapping[num] == 2:
                num_mapping.pop(num)

        return list(num_mapping.keys())[0]
        