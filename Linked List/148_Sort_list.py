# https://leetcode.com/problems/sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def merge(self, h1, h2):
        if h1 == None or h2 == None:
            if h1 == None:
                return h2
            return h1

        if h1.val < h2.val:
            h1.next = self.merge(h1.next, h2)
            return h1

        else:
            h2.next = self.merge(h1, h2.next)
            return h2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        s = head
        pre = s
        f = head

        while f and f.next:
            pre = s
            s = s.next
            f = f.next.next

        pre.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(s)
        return self.merge(h1, h2)
