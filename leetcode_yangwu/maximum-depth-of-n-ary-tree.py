#559. N 叉树的最大深度
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maxDepth = 0
        for node in root.children:
            maxDepth = max(maxDepth, self.maxDepth(node))
        return maxDepth + 1
        

        
