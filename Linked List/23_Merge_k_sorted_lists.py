# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merge = []
        for current in lists:
            while current:
                merge.append(current.val)
                current = current.next

        merge.sort()
        merge = [str(i) for i in merge]
        new = ListNode(','.join(merge))
        return new
