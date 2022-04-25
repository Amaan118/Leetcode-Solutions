# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = 0
        hash_t = 0
        for char in s:
            hash_s += ord(char)
        for char in t:
            hash_t += ord(char)
        l1 = list(s)
        l1.sort()
        l2 = list(t)
        l2.sort()
        return hash_s == hash_t and l1 == l2
