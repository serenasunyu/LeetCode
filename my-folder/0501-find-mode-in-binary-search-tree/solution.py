# Definition for a binary tree node.
# class TreeNode:
    # def __init__(self, val=0, left=None, right=None):
    #     self.val = val
    #     self.left = left
    #     self.right = right
class Solution:

    '''
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Defines a helper function to perform an in-order traversal of the BST. It takes a node and a dictionary (freq_dict) as input
        def in_order_traversal(node, freq_dict):
            if not node:
                return
            # Recursively calls the function on the left child of the current node, visiting nodes in ascending order
            in_order_traversal(node.left, freq_dict)
            # If the node's value is already a key in the dictionary, it increments the frequency by 1. If the node's value is not in the dictionary, it adds the value as a key with a frequency of 1
            freq_dict[node.val] = freq_dict.get(node.val, 0) + 1
            # Recursively calls the function on the right child of the current node, continuing the in-order traversal
            in_order_traversal(node.right, freq_dict)
        # edge case: If the tree is empty, the function returns an empty list 
        if not root:
            return []

        # Dictionary to store frequencies of elements
        freq_dict = {}
        in_order_traversal(root, freq_dict)

        # Find the maximum frequency
        max_freq = max(freq_dict.values())
        modes = [key for key, value in freq_dict.items() if value == max_freq]

        return modes
    '''

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def in_order(root):
            if root is None:
                return 0
            in_order(root.left)
            values.append(root.val)
            in_order(root.right)

        values = []
        in_order(root)
        
        freq_count = Counter(values)
        max_freq = max(freq_count.values())
        
        return [i for i in freq_count if freq_count[i] == max_freq]   
