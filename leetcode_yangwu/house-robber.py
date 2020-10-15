#198. 打家劫舍
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = 0
        cur = 0
        for num in nums:
            pre, cur = cur, max(cur, pre + num)
        return cur
