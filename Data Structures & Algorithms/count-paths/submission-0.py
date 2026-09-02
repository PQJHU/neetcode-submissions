class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_counter_matrx = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r==0 or c==0:
                    path_counter_matrx[r][c] = 1
                else:
                    path_counter_matrx[r][c] = path_counter_matrx[r-1][c] + path_counter_matrx[r][c-1]

        return path_counter_matrx[m-1][n-1]
        