#680. 验证回文字符串 Ⅱ
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.checkPalindrome(s, left+1, right) or self.checkPalindrome(s, left, right-1)
        return True

    def checkPalindrome(self, s, left, right):  #判断字符串的某个区间是否是回文串
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
