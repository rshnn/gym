


def minSubArrayLen(target, nums): 

    if len(nums) == 0: 
        return None

    if len(nums) == 1: 
        return 1 if nums[0] == target else None 

    # start, stop, length 
    curr_best = [0, 0]

    left = 0 
    right = 0  

    while left < len(nums): 

        running_sum = 0 

        while right < len(nums): 
            running_sum += nums[right]

            if running_sum == target: 
                # check against curr_best 
                if curr_best[1] < right - left: 
                    curr_best = [left, right-left+1]  

            elif running_sum > target: 
                # switch to incrementing left 
                break 
            else: 
                right += 1 

        while left < len(nums): 

            running_sum -= nums[left] 
            left += 1 

            if running_sum == target: 
                # check against curr_best 
                if curr_best[1] < right - left: 
                    curr_best = [left, right-left]  
            
            elif running_sum < target: 
                # back to incrementing right 
                break 
            else: 
                left += 1 




nums = [2,3,1,2,4,3]  

print(fourSum(nums))

