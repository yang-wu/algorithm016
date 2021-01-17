#62. 不同路径
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]
        for i in range(1, m):        # 第0行默认都是1种走法
            for j in range(1, n):    #第0列默认都是1种走法
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

