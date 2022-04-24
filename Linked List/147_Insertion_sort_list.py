# https://leetcode.com/problems/insertion-sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def get_len(self, head):
        fast = head
        size = 0

        while fast and fast.next:
            size += 2
            fast = fast.next.next

        if fast:
            return size+1
        return size

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = ListNode(head.val)

        while head.next:
            head = head.next
            ptr = sorted_list

            while ptr.next and ptr.val < head.val:
                ptr = ptr.next

            if head.val <= ptr.val:
                ptr.next = ListNode(ptr.val, ptr.next)
                ptr.val = head.val
            else:
                ptr.next = ListNode(head.val)

        return sorted_list
