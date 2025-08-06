from ftplib import all_errors

# Program for finding largest element in the Array.

def largest_ele(arr):

    high = arr[0]

    for num in arr:
        if num > high:
            high = num

    return high

arr=[1,2,3,4,5]
print(largest_ele(arr))