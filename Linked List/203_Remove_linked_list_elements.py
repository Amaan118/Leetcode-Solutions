# https://leetcode.com/problems/remove-linked-list-elements/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head and head.val == val:
            # print(head.val)
            head = head.next
        # print(head)
        if head:
            cn = head.next
            pn = head

            while cn:
                if cn.val == val:
                    pn.next = cn.next
                    cn = cn.next
                else:
                    cn = cn.next
                    pn = pn.next
        return head
