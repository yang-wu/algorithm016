#485. 最大连续1的个数
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count) 
                count = 0
        return max(maxCount, count) 
