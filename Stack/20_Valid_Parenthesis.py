# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        combo = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for par in s:
            if par in ['[', '{', '(']:
                stack.append(par)
                
            elif par in combo:
                if stack:
                    if combo[par] != stack.pop():
                        return False
                else:
                    return False
            
        return len(stack)==0