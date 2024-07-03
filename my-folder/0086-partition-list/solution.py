# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sml_dummy, big_dummy = ListNode(0), ListNode(0)
        sml, big = sml_dummy, big_dummy
        curr = head

        while curr:
            if curr.val < x:
                sml.next = curr
                sml = sml.next
            else:
                big.next = curr
                big = big.next
            
            curr = curr.next
        
        sml.next = big_dummy.next
        big.next = None

        return sml_dummy.next
                

        
