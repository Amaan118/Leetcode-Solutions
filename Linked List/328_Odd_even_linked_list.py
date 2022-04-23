# https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head

        odd = head
        temp = head.next
        while odd.next and odd.next.next:
            even = odd.next
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
        odd.next = temp
        return head
