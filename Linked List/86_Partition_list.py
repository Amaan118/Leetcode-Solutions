# https://leetcode.com/problems/partition-list/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        current = head
        big = ListNode(0)
        h2 = big

        temp = None

        while current:
            if current.val >= x:
                big.next = ListNode(current.val)
                big = big.next
            else:
                if temp == None:
                    h1 = current
                elif temp:
                    temp.next = current
                temp = current
            current = current.next

        if temp:
            temp.next = h2.next

            return h1
        return head
