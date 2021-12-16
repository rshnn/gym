


from collections import deque 

def sortedSquaredArray(array):
    
    left = 0 
    right = len(array)-1 

    out = deque() 

    while left <= right: 

        if abs(array[left]) > abs(array[right]): 
            out.appendleft(array[left] **2)
            left += 1
        else: 
            out.appendleft(array[right] **2)
            right -= 1 

    return list(out) 



array = [-10, 0, 10] 
print(sortedSquaredArray(array)) 

