#3. 无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sset = set()
        j = -1
        maxsize = 0
        for i in range(n):
            if i > 0:
                sset.remove(s[i-1])
            while j + 1 < n and s[j+1] not in sset:
                sset.add(s[j+1])
                j += 1
            size = j - i + 1
            maxsize = max(maxsize, size)
        return maxsize
