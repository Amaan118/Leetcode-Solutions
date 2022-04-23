# https://leetcode.com/problems/add-two-numbers-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def get_len(self, head):
        size = 0
        fast = head
        while fast and fast.next:
            size += 2
            fast = fast.next.next

        if fast:
            return size+1
        return size

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ''
        h1 = l1
        while h1:
            s1 += str(h1.val)
            h1 = h1.next

        s2 = ''
        h2 = l2
        while h2:
            s2 += str(h2.val)
            h2 = h2.next

        s3 = str(int(s1)+int(s2))

        h3 = ListNode(0)
        l3 = h3
        for char in s3:
            l3.next = ListNode(int(char))
            l3 = l3.next

        return h3.next
