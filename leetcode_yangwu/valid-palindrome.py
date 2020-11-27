#125. 验证回文串
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            while left < right and not s[left].isdigit() and not s[left].isalpha():  #既不是数字也不是字母，跳过
                left += 1
            while left < right and not s[right].isdigit() and not s[right].isalpha():
                right -= 1
            if left < right:
                if s[left].lower() == s[right].lower(): #不区分大小写
                    left += 1
                    right -= 1
                else:
                    return False
        return True
            
