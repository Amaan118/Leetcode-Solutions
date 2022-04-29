# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [0]*len(prices)
        stack = list()

        for i in range(len(prices)-1, -1, -1):
            while len(stack) > 0 and stack[-1] > prices[i]:
                stack.pop()

            if len(stack) == 0:
                ans[i] = prices[i]
            else:
                ans[i] = prices[i] - stack[-1]

            stack.append(prices[i])

        return ans
