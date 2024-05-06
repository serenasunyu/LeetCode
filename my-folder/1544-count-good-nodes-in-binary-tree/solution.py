# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, mx=-inf) -> int:
        if not root:
            return 0
        left = self.goodNodes(root.left, max(mx, root.val))
        right = self.goodNodes(root.right, max(mx, root.val))

        return left + right + (mx <= root.val)





        # counter = [0]

        # def dfs(node, maxValue):
        #     if not node:
        #         return

        #     if node.val >= maxValue:
        #         counter[0] += 1
        #         maxValue = node.val

        #     dfs(node.left, maxValue)
        #     dfs(node.right, maxValue)

        # dfs(root, float('-inf'))
        # return counter[0]

        # def dfs(node, maxValue):
        #     if not node:
        #         return 0

        #     count = 0
        #     if node.val >= maxValue:
        #         count = 1

        #     left_count = dfs(node.left, max(maxValue, node.val))
        #     right_count = dfs(node.right, max(maxValue, node.val))

        #     return left_count + right_count + count

        # return dfs(root, float('-inf'))


