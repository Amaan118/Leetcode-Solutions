# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        outstr = ''

        slow = head
        while slow:
            outstr += str(slow.val)
            slow = slow.next

        if len(outstr) == 1:
            return True
        if len(outstr) % 2 != 0:
            return outstr[:len(outstr)//2] == outstr[len(outstr)//2+1:][::-1]
        return outstr[:len(outstr)//2] == outstr[-len(outstr)//2:][::-1]
