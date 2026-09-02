class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combines = []

        def back_tracking(sum: int, comb: list[int], starter: int):

            if sum < target:
                for candidate in nums[starter:]:
                    comb.append(candidate)
                    if candidate != nums[starter]:
                        starter += 1
                    back_tracking(sum + candidate, comb, starter)
                    popped =comb.pop()
                    if popped != candidate:
                        starter -= 1
            elif sum > target:
                return
            else:
                combines.append(comb[:])
                return

        for i in range(len(nums)):
            comb = [nums[i]]  # start
            back_tracking(nums[i], comb, i)
        return combines
        