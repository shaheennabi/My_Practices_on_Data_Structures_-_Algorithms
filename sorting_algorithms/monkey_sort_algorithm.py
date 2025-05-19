# Sorting

def is_sorted(arr):

    sorted = True

    for i in range(len(arr) - 1):
        if arr[i]>arr[i + 1]:
            sorted = False
    return sorted
    
            


# Monkey sort
import random
import time

def monkey_sort(arr):

    while not is_sorted(arr):
        random.shuffle(arr)
        print(arr)
    print(arr)

monkey_sort([12,33,42,2,45])