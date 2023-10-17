from queue import Queue
class Solution:
    """
    def isBinaryTreeValid(self, root: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        visited = [False] * len(leftChild) # track visited nodes
        nodeQueue = Queue() # queue for BFS traversal
        nodeQueue.put(root)
        visited[root] = True

        while not nodeQueue.empty():
            current = nodeQueue.get()

            # check left child
            if leftChild[current] != -1:
                if visited[leftChild[current]]: # check cycle
                    return False

                nodeQueue.put(leftChild[current])
                visited[leftChild[current]] = True # makr left child as visited

            # check right child
            if rightChild[current] != -1:
                if visited[rightChild[current]]: # check cycle
                    return False

                nodeQueue.put(rightChild[current])
                visited[rightChild[current]] = True # makr left child as visited
        # check if there are multiple components
        for visit in visited:
            if not visit:
                return False
        return True # all nodes form a valid binary tree

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        childCount = [False] * n # tracks child count for each node

        # update child count based on leftChild
        for child in leftChild:
            # check if node has child
            if child != -1:
                childCount[child] = True # mark left child as having a parent

        # update child count based on rightChild
        for child in rightChild:
            if child != -1:
                if childCount[child]: # check if the right child already has a parent
                    return False
                
                childCount[child] = True

        root = -1 # root node
        for i in range(n):
            if not childCount[i]:
                if root == -1:
                    root = i # set root node if not assigned

                else:
                    return False # multiple roots found, not a valid binary tree

        if root == -1:
            return False # no root found, not a valid binary tree
        
        return self.isBinaryTreeValid(root, leftChild, rightChild) # check if the tree is valid
    """

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # identify the root
        root = 0
        children = set(leftChild + rightChild)
        for i in range(n):
            if i not in children:
                root = i
        # breadth-first search traversal starting from the root node
        visited = [False] * n # track of visited nodes
        num = 0 # count the number of nodes visited
        q = [root] # track of the nodes to be visited
        while q:
            curr = q.pop(0)
            if visited[curr]:
                return False

            visited[curr] = True
            num += 1

            l, r = leftChild[curr], rightChild[curr]
            if l != -1:
                q.append(l)
            if r != -1:
                q.append(r)
        # if th etotal number of visited nodes equals the total number of nodes in the tree, it means all nodes have been visted and the binary tree is valid
        return num == n 
