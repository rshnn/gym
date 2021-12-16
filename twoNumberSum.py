


def twoNumberSum(array, targetSum):
    
    looking_for = dict() 

    for idx, item in enumerate(array): 

        if targetSum - item in looking_for.keys(): 
            return targetSum-item, item  

        else: 
            looking_for[item] = idx 

    return list()  



arr = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10 
print(twoNumberSum(arr, targetSum))