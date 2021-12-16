


def binarysearch(target, array): 

    if not array: 
        return False 

    left = 0 
    right = len(array)-1 

    while left <= right: 

        mid = left + ((right-left) // 2)

        if array[mid] == target:
            return True

        elif target < array[mid]: 
            # search to the left 
            right = mid - 1 

        else: 
            # search to the right  
            left = mid + 1 

    return False 


def threeNumberSum(array, targetSum):
    # Write your code here.
    
    if len(array) < 3: 
        return list()


    array.sort() 

    left1 = 0 
    left2 = 1 

    results = list() 

    while left1 < len(array) - 1: 
        left2 = left1 + 1 

        while left2 < len(array): 

            looking_for = targetSum - (array[left1] + array[left2])

            if looking_for > array[left2]: 
                if left2+1 < len(array): 
                    subarray = array[left2+1:]
                    
            else: 
                subarray = [ ]

            # found triple 
            if binarysearch(looking_for, subarray):   
                triple = [array[left1], array[left2], looking_for]
                results.append(triple)  

            else: 
                # continue onto next iteration of loop.  increment left ptrs 
                pass 

            left2 += 1 

        left1 += 1 

    return results 







a = threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
print(a) 
