# https://leetcode.com/problems/merge-in-between-linked-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        h1 = list1
        h2 = list2

        ind = 0
        while ind != b:
            if ind == a-1:
                temp = h1
            h1 = h1.next
            ind += 1

        temp.next = h2

        while h2.next:
            h2 = h2.next

        h2.next = h1.next
        return list1
