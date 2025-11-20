class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        import math
        """
        pile = array of piles, with piles[i] bananas in each
        number of eating sessions: math.ceil(piles[i]/k)
        - must be less than h
        """

        # total_hours = sum(math.ceil(pile/k) for pile in piles)

        left, right = 1, max(piles)

        # helper to check if k is valid
        def can_finish(k):
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/k) # (p + k - 1) // k is integer ceil
            return hrs <= h # bool
    
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid): # if mid works, try a smaller value
                right = mid
            else: 
                left = mid + 1

        return left

