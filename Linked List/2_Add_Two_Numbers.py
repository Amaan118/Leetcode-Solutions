# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = l1
        r2 = l2
        r3 = ListNode(0)
        temp = r3

        carry = 0
        while r1 and r2:
            if carry == 1:
                if r1.val + r2.val+1 >= 10:
                    node = ListNode((r1.val+r2.val+1) % 10)
                    temp.next = node
                else:
                    node = ListNode(r1.val+r2.val + 1)
                    temp.next = node
                    carry = 0
            else:
                if r1.val + r2.val >= 10:
                    node = ListNode((r1.val+r2.val) % 10)
                    temp.next = node
                    carry = 1
                else:
                    node = ListNode(r1.val+r2.val)
                    temp.next = node

            temp = temp.next
            r1 = r1.next
            r2 = r2.next

        while r1:
            if carry == 1:
                if r1.val+1 < 10:
                    node = ListNode(r1.val+1)
                    carry = 0
                else:
                    node = ListNode(0)
                    carry = 1
            else:
                node = ListNode(r1.val)
            temp.next = node
            temp = temp.next
            r1 = r1.next

        while r2:
            if carry == 1:
                if r2.val+1 < 10:
                    node = ListNode(r2.val+1)
                    carry = 0
                else:
                    node = ListNode(0)
                    carry = 1
            else:
                node = ListNode(r2.val)
            temp.next = node
            temp = temp.next
            r2 = r2.next

        if carry == 1:
            node = ListNode(1)
            temp.next = node

        return r3.next
