
# Program to shift the array to left by one element

def left_rotate(arr):
    first = arr[0]

    for i in range(1,len(arr)):
        arr[i-1] = arr[i]

    arr[-1] = first
    return arr

arr = [10,20,30,40]
print(left_rotate(arr))