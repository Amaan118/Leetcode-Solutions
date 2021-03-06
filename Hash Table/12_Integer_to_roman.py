# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        while num != 0:
            if num >= 1000:
                num = num - 1000
                roman += 'M'

            elif num >= 900:
                num = num - 900
                roman += 'CM'

            elif num >= 500:
                num = num - 500
                roman += 'D'

            elif num >= 400:
                num = num - 400
                roman += 'CD'

            elif num >= 100:
                num = num - 100
                roman += 'C'

            elif num >= 90:
                num = num - 90
                roman += 'XC'

            elif num >= 50:
                num = num - 50
                roman += 'L'

            elif num >= 40:
                num = num - 40
                roman += 'XL'

            elif num >= 10:
                num = num - 10
                roman += 'X'

            elif num >= 9:
                num = num - 9
                roman += 'IX'

            elif num >= 5:
                num = num - 5
                roman += 'V'

            elif num >= 4:
                num = num - 4
                roman += 'IV'

            else:
                num -= 1
                roman += 'I'

        return roman
