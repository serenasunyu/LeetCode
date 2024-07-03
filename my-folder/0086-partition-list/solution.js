/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    // partition the linked list into two separte lists and create dummy nodes for the lists
    let small = new ListNode(0);
    const smallHead = small;
    let large = new ListNode(0);
    const largeHead = large;

    // iterate through the given list and append nodes to either small or large list
    while (head !== null) {
        if (head.val < x) {
            small.next = head;
            small = small.next;
        } else {
            large.next = head;
            large = large.next;
        }

        head = head.next;
    }

    large.next = null; // end the large list, because in the original list, large.next may point to the other node that smaller than the given node
    small.next = largeHead.next; // connect small list to th elarge list

    return smallHead.next; // return the head of the partitioned list
};
