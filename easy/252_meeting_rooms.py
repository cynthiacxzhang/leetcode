class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        # sorting by start time
        sorted_meetings = sorted(intervals, key=lambda meeting: meeting[0])

        for i in range(1, len(sorted_meetings)): 

            # if start of curr is before end of prev
            if sorted_meetings[i][0] < sorted_meetings[i - 1][1]:
                return False
        
        return True
            
