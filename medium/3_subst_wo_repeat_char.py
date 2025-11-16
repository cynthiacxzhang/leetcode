class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force: generate all substrings & update max length
        # better: sliding window, set for dupe check

        subst = set()
        
        max_len = 0
        left = 0

        for right in range(len(s)):
            if s[right] in subst:
                while s[right] in subst:
                    subst.discard(s[left])
                    left +=1
            subst.add(s[right])
            max_len = max(max_len, len(subst))
            right += 1
        
        return max_len
                    
        




        
        