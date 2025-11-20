class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = {}

        # building count dict
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        odd_num = 0

        for letter in freq:
            # if odd, add to count
            if freq[letter] % 2 != 0:
                # print(freq[ch])
                odd_num += 1
                # print(odd_num)
                if odd_num > 1:
                    return False
        
        return True
