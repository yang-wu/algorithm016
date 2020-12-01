#剑指 Offer 58 - II. 左旋转字符串
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        lists = list(s)
        while n:
            tmp = lists.pop(0)
            lists.append(tmp)
            n -= 1
        return ''.join(lists)
