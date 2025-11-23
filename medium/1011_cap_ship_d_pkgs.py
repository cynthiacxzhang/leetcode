class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        """
        Greedy + binary search optimization
        """

        # greedy condition - if current total weight > capacity
        # run this function on every chosen capacity number until we find min
        def can_ship(cap):
            num_days = 1
            curr = 0

            for weight in weights:
                # if capacity exceeded
                if curr + weight > cap:
                    num_days += 1
                    curr = weight # reset and add curr
                else: 
                    curr += weight 
            return num_days <= days # bool

        # bin search to find min capacity
        # capacity cannot be less than the heaviest weight
        left, right = max(weights), sum(weights)
        mid = (left + right) // 2 

        while left < right:
            if can_ship(mid) == True:
                right = mid # mid is still valid, should be included
            else:
                left = mid + 1 # mid is not valid, can cut out
            mid = (left + right) // 2 
        
        return mid




        
        


