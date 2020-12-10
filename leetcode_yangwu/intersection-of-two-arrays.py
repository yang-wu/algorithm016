#349. 两个数组的交集
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashNums1 = {}
        nums = []
        for num in nums1:
            hashNums1[num] = 1
        for num in nums2:
            if num in hashNums1.keys():
                nums.append(num)
                hashNums1.pop(num)
        return nums
