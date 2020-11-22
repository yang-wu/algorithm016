#91. 解码方法
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        if n == 1:
            if s[0] == '0':
                return 0
            else:
                return 1
        dp = [1] * n
        if s[0] == '0':
            dp[0] = 0
        else:
            dp[0] = 1
        if s[1] == '0' and s[0] == '0':
            dp[1] = 0
        elif s[1] == '0' and s[0] != '0':
            if s[0] + s[1] <= '26':
                dp[1] = 1
            else:
                dp[1] = 0
        elif s[1] != '0' and s[0] == '0':
            dp[1] = 0
        else:
            if s[0] + s[1] <= '26':
                dp[1] = 2
            else:
                dp[1] = 1
        for i in range(2, n):
            if s[i] == '0' and s[i-1] == '0':
                dp[i] = 0
            elif s[i] == '0' and s[i-1] != '0':
                if s[i-1] + s[i] <= '26':
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 0
            elif s[i] != '0' and s[i-1] == '0':
                if s[i-1] + s[i] <= '26':
                    dp[i] = dp[i-1]
            else:
                if s[i-1] + s[i] <= '26':
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[n-1]
