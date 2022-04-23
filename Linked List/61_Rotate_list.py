# https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def get_len(self, head):
        size = 0
        fast = head
        slow = head
        while fast and fast.next:
            size += 2
            slow = slow.next
            fast = fast.next.next

        if fast:
            return size+1, slow
        return size, slow

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        l, mid = self.get_len(head)
        k = k % l
        prev = head
        while prev.next != mid:
            prev = prev.next

        return head
