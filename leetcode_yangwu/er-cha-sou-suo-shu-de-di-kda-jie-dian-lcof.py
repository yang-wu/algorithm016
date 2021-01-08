#剑指 Offer 54. 二叉搜索树的第k大节点
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:      
        def dfs(root):  #按右根左深度遍历，递减排序
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            dfs(root.left)
        self.k = k
        dfs(root)
        return self.res
