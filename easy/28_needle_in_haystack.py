# Find the Index of the First Occurrence in a String

"""
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Note: solved using Python method "find"
- could also use "in", but that doesn't return the index
- using .index() raises a valueerror if not found
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """
        Brute force method: iterate through characters in the word that match first letter of needle
        - 
        """
        # Solution: use Python "in" method
        if needle in haystack:
            index = haystack.find(needle)
            return index
        else:
            return -1


        