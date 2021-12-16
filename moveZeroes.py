


def moveZeroes(nums):

    count = 0 
    i = 0 
    j = 0 

    while i < len(nums): 

        if nums[i] == 0: 
            count += 1 
        else: 
            nums[j] = nums[i] 
            j += 1 

        i += 1 

    for z in range(1, count + 1): 
        nums[-z] = 0    


if __name__ == '__main__':
    
    nums = [0, 3, 1, 3, 0 ,0, 2, 1] 
    print(moveZeroes(nums)) 
    print(nums)