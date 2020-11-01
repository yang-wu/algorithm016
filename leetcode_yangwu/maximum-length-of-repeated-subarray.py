#718. 最长重复子数组
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        n = len(A)
        m = len(B)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
        return res
