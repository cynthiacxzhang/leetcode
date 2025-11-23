class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heap = []

        # max heap, push -ve values
        for stone in stones:
            val = -(stone)
            heapq.heappush(heap, val)

        # some variables
        new, x, y = 0, 0, 0

        while len(heap) > 1:

            # double pop
            y = -1 * heapq.heappop(heap) # biggest
            x = -1 * heapq.heappop(heap) # second biggest

            # if x == y, keep the double pop since they're both destroyed

            # if x != y
            if x != y:
                new = -1*(y - x)
                heapq.heappush(heap, new)
        
        if not heap:
            return 0
        else: 
            return -1*heap[0]






        
