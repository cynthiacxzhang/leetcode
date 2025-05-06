# Repeated Substring Pattern

"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Solution premise: String Rotation (s+s) then remove first and last char should still preserve "s" in the middle of the new string
        # - then check if s is contained within the "rotated" new string
        
        return s in (s + s)[1:-1]
