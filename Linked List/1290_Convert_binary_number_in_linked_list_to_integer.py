# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        out = ''
        current = head
        while current and current.next:
            out += str(current.val)
            out += str(current.next.val)
            current = current.next.next

        if current:
            out += str(current.val)

        return int(out, 2)
