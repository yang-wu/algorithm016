#53. 最大子序和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = 0
        res = nums[0]
        for num in nums:
            if dp > 0:
                dp += num
            else:
                dp = num
            res = max(res, dp)
        return res
