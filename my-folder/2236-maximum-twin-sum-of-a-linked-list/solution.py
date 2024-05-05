# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse the first half of the linkedlist
        slow, fast = head, head
        reverse = None
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        
        first = reverse

        second = slow
        max_val = -math.inf
        while first:
            if first.val + second.val > max_val:
                max_val = first.val + second.val
            first = first.next
            second = second.next
        return max_val
