# https://leetcode.com/problems/reverse-linked-list-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = head
        i = 1
        while i < left:
            start = start.next
            i += 1

        end = start
        j = i
        while j < right:
            end = end.next
            j += 1

        init = start
        prev = end.next
        final = end.next

        while init != final:
            next = init.next
            init.next = prev
            prev = init
            init = next

        if start == head:
            head = prev
        else:
            current = head
            while current.next != start:
                current = current.next

            current.next = prev

        return head
