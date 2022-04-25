# https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        data = dict()

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if id(fast) in data:
                return True
            data[id(fast)] = 1

        return False
