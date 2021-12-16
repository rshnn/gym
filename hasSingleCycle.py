def hasSingleCycle(array):
    # Write your code here.

    count = 0 

    curr = 0 
    while count < len(array): 

        if curr == 0 and 1 < count < len(array): 
            return False 

        print(curr) 

        next_idx = jump(curr, array) 
        curr = next_idx
        count += 1 


    if curr%len(array) == 0: 
        return True
    else: 
        return False 


def jump(idx, array): 

    jump_amount = array[idx%len(array)]
    new_idx = idx + jump_amount 
    return new_idx
    



arr = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle(arr)) 