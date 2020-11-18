#442. 数组中重复的数据
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            index = abs(num) - 1   #有些值变为了负数，需要取绝对值
            if nums[index] < 0:
                res.append(abs(num))  #取绝对值
            nums[index] = - nums[index]  #遍历过的值取负数
        return res
