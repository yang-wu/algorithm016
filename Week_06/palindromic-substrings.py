#647. 回文子串
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        for j in range(len(s)):
            for i in range(len(s)):
                if i <= j:
                    if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1] == 1):
                        dp[i][j] = 1
                        res += 1
        return res

