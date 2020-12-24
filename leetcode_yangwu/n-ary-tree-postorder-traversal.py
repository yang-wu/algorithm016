#590. N叉树的后序遍历
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:  
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.mypostorder(root, res)
        return res

    def mypostorder(self, root, res=[]):
        if not root:
            return
        for node in root.children:
            self.mypostorder(node, res)
        res.append(root.val)
        return res
