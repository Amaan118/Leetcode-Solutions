# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

    def get_mid(self, head):
        pre = slow = fast = head
        size = 0
        while fast and fast.next:
            size += 2
            pre = slow
            slow = slow.next
            fast = fast.next.next

        if fast:
            return size+1, pre, slow
        return size, pre, slow

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head.next == None:
            return head

        size, bef_mid, mid = self.get_mid(head)
        new_mid = self.reverse(mid)
        bef_mid.next = new_mid

        p1 = head
        p2 = new_mid
        n = 0

        if k > size//2:
            k -= size+1

        while p1 != new_mid and p2:
            if (n+1) % k == 0:
                p1.val, p2.val = p2.val, p1.val
                break

            p1 = p1.next
            p2 = p2.next
            n += 1

        bef_mid.next = self.reverse(new_mid)
        return head
