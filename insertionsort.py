def insertionSort(array):
    # Write your code here.
    

    for i in range(1, len(array)): 

        j = i 
        while (j > 0) and (array[j-1] > array[j]): 
            tmp = array[j]
            array[j] = array[j-1]
            array[j-1] = tmp 

            j -=1 

    return array 







a = insertionSort([8, 5, 2, 9, 5, 6, 3])
assert a == [2, 3, 5, 5, 6, 8, 9] 