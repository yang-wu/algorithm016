#剑指 Offer 53 - I. 在排序数组中查找数字 I
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        count = 0
        while left <= right:
            mid = (left + right) // 2
            lmid = mid - 1
            rmid = mid + 1
            if target == nums[mid]:
                count += 1
                while rmid < n and target == nums[rmid]:
                    count += 1
                    rmid += 1
                while lmid >= 0 and target == nums[lmid]:
                    count += 1
                    lmid -= 1
                break
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return count
    

