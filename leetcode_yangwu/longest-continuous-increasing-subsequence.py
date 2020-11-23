#674. 最长连续递增序列
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        count = 1
        maxCount = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1
            maxCount = max(maxCount, count)
        return maxCount
