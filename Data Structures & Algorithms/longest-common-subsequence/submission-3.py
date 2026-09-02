class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        dp = [[0]*(l2+1) for _ in range(l1+1)]

        for r in range(1, l1+1):
            for c in range(1, l2+1):
                print(r,text1[r-1], c,text2[c-1])

                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])

        return dp[l1][l2]
