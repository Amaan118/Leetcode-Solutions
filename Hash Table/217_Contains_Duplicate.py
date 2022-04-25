# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        stack = dict()

        for i in nums:
            if i in stack:
                return True
            else:
                stack[i] = i
        return False
