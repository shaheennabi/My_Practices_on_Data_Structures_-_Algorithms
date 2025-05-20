# Function to merge two sorted arrays into a single sorted array
def merge_sorted(arr1, arr2, arr):
    i = j = k = 0

    # Merge while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    # Append remaining elements from arr1
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    # Append remaining elements from arr2
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1

# Function that implements merge sort using divide and conquer
def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the left and right halves
    merge_sort(left)
    merge_sort(right)

    # Merge the sorted halves into the original array
    merge_sorted(left, right, arr)

# Example usage
arr = [2, 1, 5, 8, 9, 7, 4, 6]
merge_sort(arr)
print("Sorted array:", arr)

# This algorithm has a time complexity of O(n log n)
# and a space complexity of O(n)
# It uses recursion based on the divide and conquer approach
