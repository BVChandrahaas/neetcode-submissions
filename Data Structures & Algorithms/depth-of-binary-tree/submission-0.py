# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def checkDepth(node):
            if not node:
                return 0 

            l = checkDepth(node.left)

            r = checkDepth(node.right)

            return 1+ max(l,r)
        
        return checkDepth(root)


        