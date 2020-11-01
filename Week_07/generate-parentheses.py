#22. 括号生成
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrace(s, left, right):
            if len(s) == 2 * n:
                res.append("".join(s))
                return
            if left < n:
                s.append("(")
                backtrace(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(")")
                backtrace(s, left, right + 1)
                s.pop()
        s = []
        left = 0
        right = 0
        backtrace(s, left, right)
        return res
