#557. 反转字符串中的单词 III
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i, word in enumerate(words):
            words[i] = word[::-1]
        return " ".join(words)
