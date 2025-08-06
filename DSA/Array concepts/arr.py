
# Linear Search

# def linear(arr,targ):
#     for i in range(len(arr)):
#         if arr[i] == targ:
#             print(i)
#
#     return -1
#
# arr=[1,2,4,3,8,5,4]
# targ = 1
# linear(arr,targ)

#Binary Search

def binary(arr,targ):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low+high // 2
        if arr[mid] == targ:
            return mid
        elif arr[mid] < targ:
            low = mid+1
        else:
            high = mid-1

    return -1

arr=[10,20,30,40,50]
targ = 30
binary(arr,targ)
