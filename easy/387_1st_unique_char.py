class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # hash map/counting
        freq = {}
        for i, ch in enumerate(s):
            freq.setdefault(ch, []).append(i)
        
        unique = [] # set default min to highest

        for val in freq:
            if len(freq[val]) == 1:
                unique.append(freq[val][0])
        
        if unique:
            return min(unique)
        
        return -1

            
        






