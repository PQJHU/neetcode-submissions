class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral_list = []
        left = 0
        up = 0
        right = len(matrix[0]) # max to n
        bottom = len(matrix) # max to m
        i = j = 0

        while left < right and up < bottom:
            up += 1
            if up <= bottom:
                for j in range(left, right): # go right
                    spiral_list.append(matrix[i][j])
                right -= 1

            if left <= right:
                for i in range(up, bottom): # go down
                    spiral_list.append(matrix[i][j])
                bottom -= 1

            if up <= bottom:  # go left only if on the new row
                for j in range(right-1, left-1, -1): # go left
                    spiral_list.append(matrix[i][j])
                left += 1

            if left <= right:
                for i in range(bottom-1, up-1, -1): # go up
                    spiral_list.append(matrix[i][j])

        return spiral_list
