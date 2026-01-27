class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        import heapq

        result = []
        new = newInterval

        # case 1: if no intervals, append curr
        if not intervals:
            result.append(new)
            return result
        
        # case 3: new is larger than all intervals - should be done by heap?

        # min heap, sorting by start times? then pushing and popping based on end times
        # push intervals into it via heap methods
        heap = []
        for interval in intervals:
            heapq.heappush(heap, interval) # push intervals into heap

        while heap:
            curr = heap[0]
            # heapq.heappop(heap) # min val is curr

            # 2 cases here

            # case 1 - if start of new precedes start of curr
            if new[0] < curr[0]:
                # 1b - if new is entirely before curr
                if new[1] < curr[0]:
                    break # want to pop the rest of the heap now
                # 1c - new[1] <= curr[0]
                else:
                    # pop curr and make new new value
                    heapq.heappop(heap)

                    lhs = min(new[0], curr[0])
                    rhs = max(new[1], curr[1])

                    new = (lhs, rhs)
                    # no need to push, element gets absorbed - so keep comparing

            # case 2 - if start of new is after or at start of curr
            if new[0] >= curr[0]:
                heapq.heappop(heap)
                # if new starts after curr ends, move along heap
                if new[0] > curr[1]:
                    result.append(curr)
                    continue
                # merging or absorbing
                lhs = curr[0]
                rhs = max(new[1], curr[1])

                new = (lhs, rhs)
        
        result.append(new)
        
        # append the rest
        while heap:
            now = heapq.heappop(heap)
            result.append(now)
        
        return result
        

                
        
        