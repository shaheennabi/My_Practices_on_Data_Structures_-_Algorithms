def bubble_sort(arr):

    for i in range(len(arr) - 1):
         for j in range(len(arr) - 1 - i):
             if arr[j] > arr[j+1]:
                 arr[j], arr[j+1] =   arr[j+1], arr[j]
    print(arr)



array =  [3,2,5,7,12,1]

bubble_sort(array)