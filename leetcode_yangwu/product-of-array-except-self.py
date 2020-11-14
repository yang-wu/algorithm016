#238. 除自身以外数组的乘积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n   #left[i]存储nums[i]左侧元素乘积
        right = [0] * n  #right[i]存储nums[i]右侧元素乘积
        res = [0] * n
        left[0] = 1      #nums[0]左侧没有元素，所以乘积为1
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        right[n-1] = 1    #nums[n-1]右侧没有元素，所以乘积为1
        for i in range(n-2, -1, -1):  #逆序遍历
            right[i] = right[i+1] * nums[i+1]
        for i in range(n):
            res[i] = left[i] * right[i]   #左侧乘积乘以右侧乘积
        return res
