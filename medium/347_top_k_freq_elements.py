class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums: 
            key = num
            freq[key] = freq.get(num, 0) + 1
        
        # bucket sort method
        # max frequency = length of array (assuming [1, 1, 1, 1])
        # need arr len + 1 buckets (to include 0)
        buckets = [[] for _ in range(len(nums) + 1)]

        # push number into frequency location
        for num, count in freq.items():
            buckets[count].append(num)

        output = []
        for count in range(len(buckets)-1, -1, -1):
            for num in buckets[count]:
                output.append(num)
                if len(output) == k:
                    return output
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

                # heaps method
        import heapq

        freq = {} # (num:count)

        for num in nums: 
            key = num
            freq[key] = freq.get(num, 0) + 1

        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        output = []
        for count, num in heap:
            output.append(num)
        
        return output
