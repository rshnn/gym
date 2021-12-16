

import math 

def binary_search_for_false(arr): 

    left = 0 
    right = len(arr) - 1 

    while left <= right: 
        mid = left + ((right - left) // 2)   
 
        if arr[mid] == False: 
            # found false, move left 
            right = mid - 1 

        else: 
            # didnt fail yet, move right 
            left = mid + 1


    return mid  



def longest_period(inp): 

    best_chain_so_far = 0 
    prev = math.inf 

    curr_chain = 0 
    for idx in range(len(inp)): 
        idx_of_first_fail = binary_search_for_false(inp[idx])

        green_perc = idx_of_first_fail / len(inp[idx])  

        if prev > green_perc: 
            curr_chain += 1 

        else: 
            best_chain_so_far = max(curr_chain, best_chain_so_far) 
            curr_chain = 1 

        prev = green_perc 

    return best_chain_so_far 






inp = [
    [True, True, True, False, False], 
    [True, True, True, True, False], 
    [True] * 6 + [False] * 3, 
    [True] * 1 + [False] * 5, 
    [True] * 12 + [False], 
    [True, False], 
    [True] * 4 + [False] * 2, 
]


print(longest_period(inp))





