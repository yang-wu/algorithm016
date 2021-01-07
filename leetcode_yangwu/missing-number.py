#268. 丢失的数字
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = 0
        sum2 = 0
        for i in range(n+1):
            sum1 += i
        for i in nums:
            sum2 += i
        return sum1 - sum2
