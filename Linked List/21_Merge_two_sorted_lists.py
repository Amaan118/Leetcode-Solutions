# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        h3 = ListNode(0)
        current = h3

        while h1 and h2:
            if h1.val < h2.val:
                current.next = h1
                h1 = h1.next
            else:
                current.next = h2
                h2 = h2.next

            current = current.next

        while h1:
            current.next = h1
            h1 = h1.next
            current = current.next

        while h2:
            current.next = h2
            h2 = h2.next
            current = current.next

        return h3.next
