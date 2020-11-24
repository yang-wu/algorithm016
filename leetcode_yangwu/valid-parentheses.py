#20. 有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in maps.keys():    #左括号入栈
                stack.append(i)
            elif stack and i == maps[stack[-1]]:  #栈不空，且当前元素和栈顶元素匹配，出栈
                stack.pop()
            else: #1.中间栈为空，且遇到右括号  2.中间栈不空且当前元素和栈顶元素不匹配
                return False
        if not stack:
            return True
        else:
            return False
