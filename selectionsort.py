import math 

def selectionSort(array):

    # Write your code here.
    
    for j in range(0, len(array)): 

        smallest = array[j], j  

        for idx in range(j+1, len(array)): 
            if smallest[0] > array[idx]: 
                smallest = array[idx], idx 

        tmp = array[j]
        array[j] = smallest[0] 
        array[smallest[1]] = tmp  

    return array 



assert selectionSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]