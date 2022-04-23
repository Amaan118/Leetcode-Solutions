# https://leetcode.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1 = headA
        h2 = headB

        ids = {}

        while h1 and h2:
            if id(h1) in ids:
                return ids[id(h1)]
            if id(h2) in ids:
                return ids[id(h2)]
            else:
                if id(h1) == id(h2):
                    return h1
                ids[id(h1)] = h1
                ids[id(h2)] = h2
            h1 = h1.next
            h2 = h2.next

        while h1:
            if id(h1) in ids:
                return ids[id(h1)]
            h1 = h1.next

        while h2:
            if id(h2) in ids:
                return ids[id(h2)]
            h2 = h2.next
        return None
