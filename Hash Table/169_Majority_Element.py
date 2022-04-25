# https://leetcode.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = {}
        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1

        high = 0
        for key in data:
            if data[key] > high:
                ans = key
                high = data[key]

        return ans
