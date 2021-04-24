def bubbleSort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

n = int(input("Enter the number of elements: "))
arr = [int(input()) for i in range(n)]
output = bubbleSort(arr)
print("sorted List", output)
"""
best case and Average Case - O(n)
Worst Case - O(n^2)
"""