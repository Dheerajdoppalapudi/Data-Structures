#linear search python code
def linearSearch(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return True
    return False

string = input("Enter the number ")
arr = [int(x) for x in string.split()]

if linearSearch(arr,element = int(input('Enter the number to be search '))):
    print("Number found ")
else:
    print("Number not found ")