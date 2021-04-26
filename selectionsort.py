def selectionSort(arr):
    for i in range(len(arr)):
        min_element = min(arr[i:])
        index_element = arr.index(min_element)
        arr[i], arr[index_element] = arr[index_element], arr[i]
    return arr

arr = [8,3,9,2,7,1,5,6]
print(selectionSort(arr))