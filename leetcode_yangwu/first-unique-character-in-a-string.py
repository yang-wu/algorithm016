#387. 字符串中的第一个唯一字符
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)   #计数散列表
        for i, val in enumerate(s):
            if cnt[val] == 1:
                return i
        return -1
