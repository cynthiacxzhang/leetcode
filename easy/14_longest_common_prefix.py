# Longest Common Prefix

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # If the input list is empty, return an empty string as there is no prefix
        if not strs:
            return ""

        # Loop through each character index of the first string in the list
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Compare this character with the character at the same index in the rest of the strings
            for s in strs[1:]:
                # If current string is shorter than i+1 or character mismatch occurs
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]
        