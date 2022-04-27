# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = list()
        stack2 = list()

        c1 = l1
        c2 = l2

        while c1:
            stack1.append(f'{c1.val}')
            c1 = c1.next

        while c2:
            stack2.append(f'{c2.val}')
            c2 = c2.next

        ans = str(int(''.join(stack1)) + int(''.join(stack2)))
        l3 = ListNode(0)
        c3 = l3

        for char in ans:
            c3.next = ListNode(int(char))
            c3 = c3.next

        return l3.next
