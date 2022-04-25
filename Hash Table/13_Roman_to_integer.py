# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'V': 5,
            'I': 1
        }

        val = 0
        romans = list(s)
        rom = 0
        while rom != len(romans):
            if romans[rom] == 'M':
                val += 1000

            elif romans[rom] == 'D':
                val += 500

            elif romans[rom] == 'C':
                if rom+1 != len(romans) and romans[rom+1] == 'M':
                    val += 900
                    rom += 1
                elif rom+1 != len(romans) and romans[rom+1] == 'D':
                    val += 400
                    rom += 1
                else:
                    val += 100

            elif romans[rom] == 'L':
                val += 50

            elif romans[rom] == 'X':
                if rom+1 != len(romans) and romans[rom+1] == 'C':
                    val += 90
                    rom += 1
                elif rom+1 != len(romans) and romans[rom+1] == 'L':
                    val += 40
                    rom += 1
                else:
                    val += 10

            elif romans[rom] == 'V':
                val += 5

            elif romans[rom] == 'I':
                if rom+1 != len(romans) and romans[rom+1] == 'V':
                    val += 4
                    rom += 1
                elif rom+1 != len(romans) and romans[rom+1] == 'X':
                    val += 9
                    rom += 1
                else:
                    val += 1
            rom += 1
        return val
