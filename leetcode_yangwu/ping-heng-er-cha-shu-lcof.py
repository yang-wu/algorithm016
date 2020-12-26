#剑指 Offer 55 - II. 平衡二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
