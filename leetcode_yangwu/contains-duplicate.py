#217. 存在重复元素
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashNums = {}
        for num in nums:
            if num not in hashNums.keys():
                hashNums[num] = 1
            else:
                return True
        return False
               
