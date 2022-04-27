# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return head

        current = head
        stack = list()

        while current:
            stack.append(current.val)
            current = current.next

        pre = new = head
        i = 0
        while new and i < len(stack):
            new.val = stack[i]
            pre = new
            if new.next:
                new.next.val = stack[len(stack)-i-1]
                new = new.next.next

            i += 1

        if len(stack) % 2:
            pre.val = stack[len(stack)//2]
        return head
