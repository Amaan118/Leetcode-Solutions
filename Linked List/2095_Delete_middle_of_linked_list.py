# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow.next:
            slow.val = slow.next.val
            slow.next = slow.next.next
        else:
            if head.next:
                head.next = None
            else:
                head = None
        return head
