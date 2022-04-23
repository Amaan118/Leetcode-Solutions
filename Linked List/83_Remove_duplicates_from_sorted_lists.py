# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = [head.val]
        # print(val)
        node = head
        nn = head.next
        while nn:
            if nn.val not in val:
                val.append(nn.val)
            else:
                node.next = nn.next
                nn = nn.next
            node = node.next
            nn = nn.next
        return head
