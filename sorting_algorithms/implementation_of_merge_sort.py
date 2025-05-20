# this is the function for merging two sorted arrays
def merge_sorted(arr1, arr2):
    i = j = 0
    merged = []

    # Merge while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append remaining elements from arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Append remaining elements from arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1 

    return merged
    

# this function implements the merge sort algorithm
# it takes an array as input and returns a sorted array
def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right =  merge_sort(right)

    return  merge_sorted(left, right)

arr = [2,1,5,8,9,7,4,6]
merge_sort(arr)

# this algorithm has the time complexity of O(n log n)
# and the space complexity of O(n)
# this algorithm uses recursion based on the divide and conquer approach