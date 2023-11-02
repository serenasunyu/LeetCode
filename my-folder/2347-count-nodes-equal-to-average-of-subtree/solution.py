# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # Initialize the result to 0
        res = 0

        def dfs(node):
            nonlocal res
            # If the node is None then return 0,0
            if not node:
                return 0, 0

            # Call the dfs function recursively on the left and right subtree and store the sum and count of the nodes
            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)

            # Calculate the sum and count of the current node by adding the value of the node with the sum and count of the left and right subtree
            curr_sum = node.val + leftSum + rightSum
            curr_count = 1 + leftCount + rightCount
            
            # If the average of the subtree is equal to the value of the node then increment the result by 1
            if curr_sum // curr_count == node.val:
                res += 1
            
            # Return the sum and count of the current node
            return curr_sum, curr_count

        # Call the dfs function on the root node
        dfs(root)
        return res

# time complexity: O(N)
# spcae complexity: O(H)
