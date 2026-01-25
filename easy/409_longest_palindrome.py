class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # frequency map
        freq = {}
        for ch in s: 
            freq[ch] = freq.get(ch, 0) + 1
        
        count = 0
        has_odd = False

        for item in freq:
            if freq[item] % 2 == 0:
                count += freq[item] # add count of that element
            else: 
                count += freq[item] - 1
                has_odd = True
        
        if has_odd:
            count += 1

        return count 

