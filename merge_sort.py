# first do sorting then merge

def msort(arr):
    if len(arr)>1:
        middle = len(arr) // 2
        left_array = arr[:middle]
        right_array = arr[middle:]
        #recursion
        msort(left_array)
        msort(right_array)
            # now merge
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged index
        while i < len(left_array) and j < len(right_array):
            if left_array[i]<right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k +=1
        while j < len(right_array):
            arr[k] = left_array[j]
            j += 1
            k +=1
     
arr_test = [64, 34, 25, 12, 22, 11, 90] 
msort(arr_test)
print(arr_test)