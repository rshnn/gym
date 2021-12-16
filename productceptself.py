


def productExceptSelf(nums): 
    
    tuple_list = list() 

    left_prod = 1 
    for item in nums: 
        tuple_list.append([left_prod, None])

        left_prod *= item 

    tuple_list[-1][1] = 1 
    right_prod = 1 

    for idx in range(len(nums)-1, -1, -1): 
        tuple_list[idx][1] = right_prod 
        right_prod *= nums[idx]


    for idx, tup in enumerate(tuple_list): 
        nums[idx] = tup[0] * tup[1] 

    return nums 



nums = [1, 2, 3, 4]
r = productExceptSelf(nums) 
print(r) 