class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_coordinates = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==0:
                    zero_coordinates.append((i,j))

        for i,j in zero_coordinates:
            matrix[i][:] = [0]*n
            for row in matrix:
                row[j] = 0
