# Roman to Integer

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Brainstorm: key is to compare values before and after based on size

        # Roman to int dictionary: 
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        value_list = []
        value = 0

        for i in range(len(s)):
            value = roman_map[s[i]]
            value_list.append(value)
            print(value_list[i])

        integer = 0

        for i in range(len(value_list)-1):
            if value_list[i] < value_list[i+1]:
                integer -= value_list[i]
            else:
                integer += value_list[i]

        # Add last value - will always be the smallest according to roman rules
        integer += value_list[-1]
    
        return integer
