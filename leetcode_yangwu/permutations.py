#46. 全排列
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        innerlist = []
        def backtrack(nums, innerlist):
            if not nums:
                return res.append(innerlist)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], innerlist + [nums[i]]) #不断拼接innerlist
        backtrack(nums, innerlist)
        return res
        
