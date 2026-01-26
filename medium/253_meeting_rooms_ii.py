class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        import heapq

        # sort meetings by start time
        # each start time gets a meeting
        # if meeting ends, room is freed 

        if not intervals:
            return 0

        # sorting meetings by start time
        meetings = sorted(intervals, key=lambda x:x[0]) 

        heap = []
        rooms = 0  
        
        for meeting in meetings:

            # if there are rooms that freed before current meeting
            if heap and heap[0] <= meeting[0]:
                heapq.heappush(heap, meeting[1]) # push new meeting's end time
                heapq.heappop(heap) # pop meeting that ended, no need for room allocation
                continue
            # if no free rooms
            if not heap or heap[0] > meeting[0]:
                rooms += 1
                heapq.heappush(heap, meeting[1]) # push new meeting's end time
                continue
    
        return rooms


            

            

        

            


