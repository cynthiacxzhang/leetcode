# max value in an array

def max_arr_val(arr):
    max_val = arr[0] 

    size = len(arr)

    for n in range(size-1):
        if n > size-1:
            break
        max_val = max(arr[n], max_val)
        n += 1
    
    return max_val

arr = [6, 12, 5, 4, 10, 3, 9]
print(max_arr_val(arr))