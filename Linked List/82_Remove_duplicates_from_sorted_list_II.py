# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        current = head
        dups = dict()
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
                dups[current.val] = 1
            else:
                current = current.next

        new = head
        while new.next:
            if new.val in dups:
                new.val = new.next.val
                new.next = new.next.next
            else:
                new = new.next

        if new.val in dups:
            if new == head:
                head = None
            else:
                c = head
                while c.next.val != new.val:
                    c = c.next
                c.next = None
        return head
