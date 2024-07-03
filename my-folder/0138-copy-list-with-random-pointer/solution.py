"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        """
        if not head: return 

        dic = {}

        curr = head
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        while curr:
            dic[curr].next = dic.get(curr.next)
            dic[curr].random = dic.get(curr.random)
            curr = curr.next

        return dic[head]
        """

        if not head: return

        curr = head

        while curr:
            temp = Node(curr.val)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = res = head.next
        prev = head

        while curr.next:
            prev.next = prev.next.next
            curr.next = curr.next.next
            prev = prev.next
            curr = curr.next
        prev.next = None
        return res
        
