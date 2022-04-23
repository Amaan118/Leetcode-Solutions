# https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def get_mid(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return head
        h1 = head
        mid = self.get_mid(head)

        temp = h1
        while temp.next != mid:
            temp = temp.next

        h2 = self.reverse(mid)
        temp.next = h2
        newMid = h2

        while h1.next != newMid and h2:
            n1 = h1.next
            h1.next = h2
            n2 = h2.next
            h2.next = n1
            h1 = n1
            h2 = n2

        h1.next = h2

    def reverse(self, head):
        current = head
        temp = None
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev
