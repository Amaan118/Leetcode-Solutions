# https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        for i in nums1:
            if i in nums2:
                inter.append(i)
                nums2.remove(i)
        return inter
