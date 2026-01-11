# Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge arrays sorted, find median value of final

        # merge sort - two pointer method
        i, j = 0, 0
        new_arr = []

        # constructing sorted array
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_arr.append(nums1[i])
                i += 1
            elif nums1[i] == nums2[j]:
                new_arr.append(nums1[i])
                i += 1
                new_arr.append(nums2[j])
                j += 1
            else: 
                new_arr.append(nums2[j])
                j += 1
        
        # extending arr based on which one still has values
        # only the array that remains will add values
        new_arr.extend(nums1[i:])
        new_arr.extend(nums2[j:])

        length = len(new_arr)
        
        if length%2 == 0:
            r = length // 2
            l = r - 1
            median = (new_arr[r] + new_arr[l]) / 2
        else:
            median = new_arr[length // 2]
        
        return median


            






        


