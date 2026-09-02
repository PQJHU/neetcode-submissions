class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        row_0_zeros = any([ele == 0 for ele in matrix[0][:]])
        col_0_zeros = any([row[0]== 0 for row in matrix])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] ==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i][1:n] = [0] * (n-1)

        for j in range(1, n):
            if matrix[0][j] == 0:
                for row in matrix[1:]:
                    row[j] = 0

        if row_0_zeros:
            matrix[0][:] = [0] * n

        if col_0_zeros:
            for row in matrix:
                row[0] = 0
