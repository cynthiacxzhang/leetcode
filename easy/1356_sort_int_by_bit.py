class Solution:
    # def sortByBits(self, arr: List[int]) -> List[int]:

    #     new_arr = {}
    #     for num in arr:
    #         val = str(bin(num)[2:])
    #         sum = 0
    #         for ch in val:
    #             if ch == '1':
    #                 sum += 1
    #             else:
    #                 sum += 0

    #         new_arr.setdefault(sum, []).append(num)
    #         new_arr[sum] = sorted(new_arr[sum])
        
    #     print(new_arr)

    #     final = []
    #     for thing in sorted(new_arr):
    #         final.extend(sorted(new_arr[thing]))

    #     return final

    # optimal solution
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))