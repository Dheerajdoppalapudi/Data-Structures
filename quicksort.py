# quick sort python program

def quicksort(arr,l,h):
 i=l-1
 pivot=arr[h]

 for j in range(l,h):
   if arr[j]<=pivot:
     i=i+1
     arr[i],arr[j] = arr[j],arr[i]
 arr[i+1],arr[h] = arr[h],arr[i+1]
 return i+1

def quicksort1(arr,l,h):
  if len(arr)==1:
    return arr
  if l<h:
    a=quicksort(arr,l,h)
    quicksort1(arr,l,a-1)
    quicksort1(arr,a+1,h)


arr = [6,2,8,3,9,4,7,5]
n=len(arr)
quicksort1(arr,0,n-1)
for i in range(n):
  print(arr[i], end=" ")