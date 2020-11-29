#58. 最后一个单词的长度
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n-1, -1, -1):
            if s[i] == ' ':
                continue
            else:
                count += 1
            if s[i] != ' ' and s[i-1] == ' ':
                break
        return count

        
