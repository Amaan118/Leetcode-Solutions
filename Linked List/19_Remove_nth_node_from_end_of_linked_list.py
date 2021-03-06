# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            head = None
            return head

        stay = head
        move = head
        for i in range(n):
            move = move.next

        if move == None:
            return head.next

        while move.next:
            move = move.next
            stay = stay.next

        stay.next = stay.next.next
        return head
