# Rotate a String

"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

"""

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        # Brainstorm
        """
        Shift a string right by one character in a loop
        For loop for # of shifts (however many characters) there are in string
        To extract last letter and append it at the beginning
        string[:k] -> gets last letter
        string[k:] -> inserts at the front of the string

        """

        for i in range(len(s)):
            s = s[len(s)-1:] + s[0:len(s)-1]
            print(s)
            if s == goal:
                return True
            i += 1
        return False
        