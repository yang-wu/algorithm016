学习笔记

1.二分查找的代码模版：
//首先数组必须是有序数组
def get(self, nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
2.贪心算法总是通过最优局部解来求最终最优解，动态规划需要记录中间状态

3.python 的除法 / 和 //区别：
  1）9 / 2 = 4.5
  2) 9 // 2 = 4  (向下取整)
  3) -9 // 2 = -5 （向下取整）
  
 4.二叉树的BFS是深度遍历左子树和右子树，二维网格的BFS是深度遍历某个节点的上、下、左、右节点。

   
