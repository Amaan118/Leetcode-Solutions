# https://leetcode.com/problems/merge-nodes-in-between-zeros/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next:
            if current.val == 0:
                temp = current.next
                tot = 0
                while temp.val != 0:
                    tot += temp.val
                    temp = temp.next
                current.next.val = tot
                current.next.next = temp
                current = temp

        new = head.next
        while new:
            new.next = new.next.next
            new = new.next

        return head.next
