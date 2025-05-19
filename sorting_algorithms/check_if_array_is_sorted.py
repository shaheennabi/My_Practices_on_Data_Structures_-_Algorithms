# Sorting

def is_sorted(arr):

    sorted = True

    for i in range(len(arr) - 1):
        if arr[i]>arr[i + 1]:
            sorted = False
    return sorted
    
            