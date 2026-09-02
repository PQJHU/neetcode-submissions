class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            to_find = target - numbers[i]
            left = i+1
            right = len(numbers) - 1
            while left <= right:
                mid = (right + left) // 2
                if numbers[left] == to_find:
                    return [i+1, left+1]
                if numbers[right] == to_find:
                    return [i+1, right +1]
                if numbers[mid] == to_find:
                    return [i+1, mid+1]
                if to_find > numbers[mid]:
                    left = mid + 1
                if to_find < numbers[mid]:
                    right = mid-1
