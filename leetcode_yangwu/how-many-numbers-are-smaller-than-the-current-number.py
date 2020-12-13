#1365. 有多少小于当前数字的数字
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freqNums = [0] * 101  #初始化长度为101的数组，统计数字出现频率
        for num in nums:
            freqNums[num] += 1  #数值作为频率下标
        for i in range(1, len(freqNums)):
            freqNums[i] = freqNums[i] + freqNums[i-1]  #小于当前数字的数量等于前1个小标频率值加上当前下标频率值
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res[i] = freqNums[nums[i]-1]
        return res
            
