 



def twoSum_(numbers, target):
    
    looking_for = dict() 

    for idx, val in enumerate(numbers): 

        if target-val in looking_for.keys(): 
            return looking_for[target-val] + 1 , idx + 1  

        else: 
            looking_for[val] = idx 

    return -1  

def twoSum(numbers, target):
    
    looking_for = dict() 

    for idx, val in enumerate(numbers): 

        if target-val in looking_for.keys(): 
            return looking_for[target-val] + 1 , idx + 1  

        else: 
            looking_for[val] = idx 

    return -1  



if __name__ == '__main__':
    numbers = [-1, 0]   
    target = -1

    print(twoSum(numbers, target))