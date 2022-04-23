# https://leetcode.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        # nex = head.next

        while current:
            if current and current.next:
                temp = current.next
                temp.next = current
                current.next = temp.next

            current = current.next.next
        return head
