def selection_sort(arr):

    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    print(arr) 


array =  [3,2,5,7,12,1]
selection_sort(array)