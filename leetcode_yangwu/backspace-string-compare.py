#844. 比较含退格的字符串
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS = []
        stackT = []
        for s in S:
            if stackS and s == '#':
                stackS.pop()
            elif s != '#':
                stackS.append(s)
        for t in T:
            if stackT and t == '#':
                stackT.pop()
            elif t != '#':
                stackT.append(t)
        return ''.join(stackS) == ''.join(stackT)

