# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inOrder(root, v):
            if root:
                inOrder(root.left, v)
                if not root.left and not root.right:
                    v.append(root.val)
                inOrder(root.right, v)

        v1, v2 = [], []
        inOrder(root1, v1)
        inOrder(root2, v2)

        return v1 == v2
