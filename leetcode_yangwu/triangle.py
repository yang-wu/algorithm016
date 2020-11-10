#120. 三角形最小路径和
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        m = len(triangle)
        dp = [[0] * m for i in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(0, i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[m-1])
