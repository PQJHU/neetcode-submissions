class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        head_row = 0
        tail_row = m-1
        target_row = 0
        while head_row<=tail_row:
            mid_row = (head_row+ tail_row)//2
            if target < matrix[mid_row][0]:
                tail_row = mid_row -1
            elif target > matrix[mid_row][n-1]:
                head_row = mid_row +1
            else:
                # head_row = tail_row = mid_row
                target_row = mid_row
                break

        head_col, tail_col = 0, n-1
        while head_col<=tail_col:
            mid_col = (head_col + tail_col)//2
            if target < matrix[target_row][mid_col]:
                tail_col = mid_col -1
            elif target > matrix[target_row][mid_col]:
                head_col = mid_col + 1
            else:
                return True
        return False
        