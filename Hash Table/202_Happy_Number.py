# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            if n in nums:
                return False
            nums.add(n)
            tot = 0
            while n:
                rem = n % 10
                tot += rem*rem
                n //= 10
            n = tot
        return True
