#219. 存在重复元素 II
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashNums = {}
        for i, num in enumerate(nums):
            if num in hashNums.keys() and i - hashNums[num] <= k: 
                return True
            else:
                hashNums[num] = i
        return False
