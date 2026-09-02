import itertools

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        col_val_hashing = [set() for _ in range(size)]
        row_val_hashing = [set() for _ in range(size)]
        block_val_hashing = [[set() for _ in range(size // 3)] for _ in range(size // 3)]

        for r in range(size):
            for c in range(size):
                num = board[r][c]
                if num == '.':
                    continue
                if num in col_val_hashing[c]:
                    return False
                if num in row_val_hashing[r]:
                    return False
                if num in block_val_hashing[r//3][c//3]:
                    return False

                col_val_hashing[c].add(num)
                row_val_hashing[r].add(num)
                block_val_hashing[r//3][c//3].add(num)

        return True
        