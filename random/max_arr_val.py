# max value in an array

def max_arr_val(arr):
    curr = arr[0]
    max_val = curr 

    size = len(arr)

    for n in arr:
        if n > size-1:
            break
        curr = arr[n]
        max_val = max(curr, max_val)
    
    return max_val
        