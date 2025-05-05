# Palindrome

"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Input: int
Output: bool

"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        """
        Logic: reverse string then check equality
        """
        # case 1: if negative
        if x < 0:
            return False
        else:
            # rest of the solution
            string_num = str(x)
            rev_string = string_num[::-1]
            return string_num == rev_string
        
        