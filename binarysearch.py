


def binarySearch(array, target):
    # Write your code here.
    
    left = 0 
    right = len(array)-1 

    while left <= right: 
        mid = left + ((right - left) // 2)

        if target == array[mid]: 
            return mid 
        elif target < array[mid]:  
            right = mid - 1 

        else: 
            left = mid + 1 

    return -1 





a = binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33)
print(a) 