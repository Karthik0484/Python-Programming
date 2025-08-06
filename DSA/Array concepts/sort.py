
# Checking whether given array is sorted or not.

def sorted_arr(arr):

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            print('Array is not sorted.')

    print('Array is sorted.')

arr=[10,20,30,40,50]

sorted_arr(arr)

