#541. 反转字符串 II
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        res = list(s)
        for i in range(0, n, 2 * k):
            res[i:i+k] = reversed(res[i:i+k])
        return "".join(res)
        
