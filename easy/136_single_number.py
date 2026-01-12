# Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for count in freq:
            if freq[count] == 1:
                return count
                