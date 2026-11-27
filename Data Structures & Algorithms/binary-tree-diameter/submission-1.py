# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        order = []
        while stack:
            node = stack.pop()
            order.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        order.reverse()

        heights = {}
        max_diameter = 0

        for node in order:
            l = heights.get(node.left, 0)
            r = heights.get(node.right, 0)
            max_diameter = max(max_diameter, l+r)
            heights[node] = 1+max(l,r)
            
        return max_diameter


        