# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        data = dict()
        if len(pattern) != len(s.split()):
            return False
        for c1, c2 in zip(pattern, s.split()):
            if c1 not in data and c2 not in data.values():
                data[c1] = c2
            else:
                if data.get(c1) != c2:
                    return False
        return True
