# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        arr = list()
        while current:
            arr.append(current.val)
            current = current.next

        arr[k-1], arr[len(arr)-k] = arr[len(arr)-k], arr[k-1]

        i = 0
        newHead = head
        while newHead:
            newHead.val = arr[i]
            newHead = newHead.next
            i += 1

        return head
