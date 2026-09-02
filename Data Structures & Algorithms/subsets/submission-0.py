import itertools as it

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for k in range(n + 1):
            # C(n,k), k=0,...n
            combines = it.combinations(range(n), k)
            for comb in combines:
                res.append([nums[j] for j in comb])

        return res
        