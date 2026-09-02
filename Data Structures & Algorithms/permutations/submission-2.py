class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)
        used = set()

        def find_permutation(path: list[int]):
            if len(path) == n:
                permutations.append(path[:])
                return
            for i in range(n):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                find_permutation(path=path)
                path.pop()
                used.remove(nums[i])

        find_permutation(path=[])
        return permutations
