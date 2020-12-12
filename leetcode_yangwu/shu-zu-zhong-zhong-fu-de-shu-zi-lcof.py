#剑指 Offer 03. 数组中重复的数字
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashNums = {}
        for num in nums:
            if num not in hashNums.keys():
                hashNums[num] = 1
            else:
                return num
