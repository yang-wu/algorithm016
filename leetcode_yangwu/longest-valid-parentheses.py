#32. 最长有效括号
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        maxlen = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i == 1:
                        dp[i] = 2
                    else:
                        dp[i] = dp[i-2] + 2
                elif s[i-1] == ')' and s[i-dp[i-1]-1] == '(' and i - dp[i-1] > 0:
                    if i - dp[i-1] >= 2:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
            maxlen = max(maxlen, dp[i])
        return maxlen
            
