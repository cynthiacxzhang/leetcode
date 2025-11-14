class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = dict()
        count_t = dict()        

        # frequency map of s
        for x in s:
            count_s[x] = count_s.get(x, 0) + 1

        # frequency map of t
        for y in t: 
            count_t[y] = count_t.get(y, 0) + 1

        # compare two frequency maps
        if count_s == count_t:
            return True

        return False
            