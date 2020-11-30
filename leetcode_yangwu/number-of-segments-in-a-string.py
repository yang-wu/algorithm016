#434. 字符串中的单词数
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                if s[i] != ' ' and s[i+1] == ' ':
                    count += 1
            else:
                if s[i] != ' ':
                    count += 1
        return count

