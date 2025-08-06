# Program to find second largest element in the array

def second_large(arr):

  # Assigning first and second largest to -infinity initially

    first = second = float('-inf')

  # Looping through the array

    for num in arr:
        if num > first:
            second = first
            first = num

        elif num > second and num != first:
            second = num

    return second

# Declaring the array and calling function

arr=[10,20,30,40,50]
print(second_large(arr))