# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverse(self, head):
        current = head
        temp = None
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head = prev

        return head

    def get_mid(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        newHead = self.get_mid(head)
        right = self.reverse(newHead)
        #right = reversed
        left = head

        # while left:
#            print(left.data, end="->")
#            left = left.next
#        print()
#
#        while right:
#            print(right.data, end="->")
#            right = right.next

        while left != newHead and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
