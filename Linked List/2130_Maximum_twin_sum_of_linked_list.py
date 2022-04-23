# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/


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

    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = self.get_mid(head)

        temp = head
        while temp.next != mid:
            temp = temp.next

        mid = self.reverse(mid)
        temp.next = mid

        newMid = temp.next
        start = head
        total = 0
        while start != newMid and newMid:
            total = max(total, start.val+newMid.val)
            start = start.next
            newMid = newMid.next

        return total
