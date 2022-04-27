# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


class Solution:
    def maxDepth(self, s: str) -> int:
        high = 0
        ans = 0
        for char in s:
            if char == '(':
                high += 1
            elif char == ')':
                high -= 1
            ans = max(ans, high)

        return ans
