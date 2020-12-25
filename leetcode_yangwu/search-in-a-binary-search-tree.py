#700. 二叉搜索树中的搜索
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while(root):
            if val == root.val:
                return root
            elif val < root.val and root.left:
                root = root.left
            elif val > root.val and root.right:
                root = root.right
            else:
                return 
        return
        
