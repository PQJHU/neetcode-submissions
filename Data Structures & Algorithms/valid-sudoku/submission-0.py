import itertools

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        col_mapping = {c:[] for c in range(size)}
        row_mapping = {r:[] for r in range(size)}
        block_mapping = {(r,c): [] for r, c in itertools.product(range(size//3), range(size//3))}
        for r in range(size):
            for c in range(size):
                num = board[r][c]
                if num == '.':
                    continue
                if num in col_mapping[c]:
                    return False
                if num in row_mapping[r]:
                    return False
                if num in block_mapping.get((r//3, c//3)):
                    return False

                col_mapping[c].append(num)
                row_mapping[r].append(num)
                block_mapping[(r//3, c//3)].append(num)

        return True
        