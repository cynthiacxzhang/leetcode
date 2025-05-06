# Check if String is Acronym of Words

"""
Given an array of strings words and a string s, determine if s is an acronym of words.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

Return true if s is an acronym of words, and false otherwise.

 

Example 1:

Input: words = ["alice","bob","charlie"], s = "abc"
Output: true
Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym. 

"""

class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        # Logic 
        """
        Pop the first character from every item in list: "words"
        Concatenate them together 
        Return string s == newly concatenated string 
        """
        current = ""
        for i in range(len(words)):
            # note: strings are immutable
            current += (words[i])[0]
        return current == s
            