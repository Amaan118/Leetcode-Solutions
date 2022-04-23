# https://leetcode.com/problems/middle-of-the-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = head
        size = 0
        while f and f.next:
            size += 2
            f = f.next.next

        if f:
            size += 1

        mid = size // 2 + size % 2

        pre = slow = head
        for i in range(0, mid):
            pre = slow
            slow = slow.next

        if size % 2:
            return pre
        return slow
