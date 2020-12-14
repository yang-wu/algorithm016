#剑指 Offer 50. 第一个只出现一次的字符
class Solution:
    def firstUniqChar(self, s: str) -> str:
        hashS = {}
        for i in s:
            if i not in hashS.keys():
                hashS[i] = 1
            else:
                hashS[i] += 1
        for index, val in hashS.items():
            if val == 1:
                return index
        return ' '
