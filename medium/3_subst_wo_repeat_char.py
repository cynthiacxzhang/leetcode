class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force: generate all substrings & update max length
        # better: sliding window, set for dupe check

        subst = set()  # track duplicates
        max_len = 0
        left = 0  # no need for right = 0 since it's init in for loop

        # right ptr passing through loop
        for right in range(len(s)):

            # if current element is already in the set, it's a duplicate
            if s[right] in subst:

                # while the current element is still a duplicate, move left ptr
                while s[right] in subst:
                    subst.discard(s[left]) # use discard as element needs to exist in set
                    left +=1
            
            # if not in set, add curr element to set
            subst.add(s[right])

            # evaluate max value
            max_len = max(max_len, len(subst))
            right += 1
        
        return max_len
                    
        




        
        