# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorder(self, root):
        ans = list()
        if root.left:
            ans.extend(self.inorder(root.left))

        ans.append(root.val)
        if root.right:
            ans.extend(self.inorder(root.right))

        return ans

    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.inorder(root)

        head = new = TreeNode(ans[0])
        for i in range(1, len(ans)):
            new.left = None
            new.right = TreeNode(ans[i])
            new = new.right

        return head
