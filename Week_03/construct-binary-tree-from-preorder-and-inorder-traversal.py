# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        leftPreorder = preorder[1:mid+1]
        leftInorder = inorder[:mid]
        rightPreorder = preorder[mid+1:]
        rightInorder = inorder[mid+1:]
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        return root
