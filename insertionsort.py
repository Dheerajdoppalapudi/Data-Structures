def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        while i >= 0 and arr[i-1] > temp:
            arr[i] = arr[i-1]
            if i == 0: # to avoid negative indexing 
                break
            i -= 1
        arr[i] = temp
    return arr

arr = [5,4,10,1,6,2]
print(insertionSort(arr))