# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

    def isEmpty(self, arr):
        return len(arr) == 0

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = list()
        rev = self.reverse(head)
        ans = list()

        temp = rev
        while temp:
            if self.isEmpty(stack):
                ans.append(0)
            else:
                while not self.isEmpty(stack) and stack[-1] <= temp.val:
                    stack.pop()
                if self.isEmpty(stack):
                    ans.append(0)
                else:
                    ans.append(stack[-1])

            stack.append(temp.val)
            temp = temp.next
        ans.reverse()
        return ans
