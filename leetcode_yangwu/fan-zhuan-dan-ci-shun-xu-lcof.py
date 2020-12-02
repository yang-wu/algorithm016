#剑指 Offer 58 - I. 翻转单词顺序
class Solution:
    def reverseWords(self, s: str) -> str:
        lists = reversed(s.split())
        return " ".join(lists)
