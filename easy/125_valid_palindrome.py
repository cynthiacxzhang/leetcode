class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = []

        for ch in s:
            if ch.isalnum():
                clean.append(ch.lower()) # lowercase, character
        
        # join back into a string
        clean = "".join(clean)
            

        left = 0
        right = len(clean) - 1

        while left < right:
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1
        
        return True




        
        