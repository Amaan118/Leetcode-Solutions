# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        data = dict()
        for c1, c2 in zip(s, t):
            if c1 not in data and c2 not in data.values():
                data[c1] = c2
            else:
                if data.get(c1) != c2:
                    return False
        return True
