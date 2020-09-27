class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(nums, tmp):
            if not nums:
                return res.append(tmp)
            for i in range(len(nums)):
                back(nums[:i] + nums[i+1:], tmp + [nums[i]])
        back(nums, [])
        return res
