# https://leetcode.com/problems/linked-list-random-node/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import random


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.data = list()
        current = head
        while current:
            self.data.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        return self.data[random.randrange(0, len(self.data))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
