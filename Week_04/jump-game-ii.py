class Solution:
    def jump(self, nums: List[int]) -> int:
        maxPos = 0
        end = 0
        step = 0
        for i in range(len(nums) - 1):
            maxPos = max(maxPos, nums[i] + i)
            if i == end:
                end = maxPos
                step += 1
        return step
