class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for item in freq:
            if freq[item] > len(nums)//2:
                return item
        
        
