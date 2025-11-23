class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heap = []

        # max heap, push -ve values
        for stone in stones:
            val = -(stone)
            heapq.heappush(heap, val)

        if len(heap) <= 1:
            last = -1*heap[0]
            return last
        
        # some variables
        new, x, y = 0, 0, 0

        while len(heap) > 1:

            # double pop
            y = -1 * heappop(heap) # biggest
            x = -1 * heappop(heap) # second biggest

            if x == y:
                continue
            
            # if x != y
            else:
                new = -1*(y - x)
                heapq.heappush(heap, new)
        
        if not heap:
            return 0
        else: 
            return -1*heap[0]






        
