#1446. 连续字符
class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        count = 1
        maxPower = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            maxPower = max(maxPower, count)
        return maxPower

