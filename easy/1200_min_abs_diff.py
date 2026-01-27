# daily 01.26.2026
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        if not arr:
            return 0
        
        arr.sort()
        print(arr)
        min_diff = arr[1] - arr[0] # placeholder

        # frequency map and finding min diff
        freq = {}

        for i in range(0, len(arr)-1):
            curr_diff = arr[i + 1] - arr[i]
            min_diff = min(curr_diff, min_diff)

            freq.setdefault(curr_diff, []).append([arr[i], arr[i+1]])
        
        return freq[min_diff]



            
        
            

