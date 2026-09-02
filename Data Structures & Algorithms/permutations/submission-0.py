class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)

        def find_permutation(path: list[int]):
            if len(path) == n:
                permutations.append(path[:])
                return
            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                find_permutation(path=path)
                path.pop()

        find_permutation(path=[])
        return permutations
        