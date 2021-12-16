


import math 



def best_block_location(blocks, reqs): 

    req_distance_list = list() 
    for req in reqs: 

        req_dist = [None] * len(blocks)

        # first pass left to right 
        left = math.inf  
        for idx, block in enumerate(blocks): 
            if block[req]: 
                req_dist[idx] = 0 
                left = 0 
            else: 
                req_dist[idx] = left + 1 


        # second pass right to left 
        right = math.inf 
        for idx_2 in range(len(blocks)-1, -1, -1): 
            
            if blocks[idx_2][req]: 
                req_dist[idx_2] = 0                 
                right = 0
                continue   

            if idx_2 == 0: 
                req_dist[idx_2] = right + 1 
                break  

            req_dist[idx_2] = min(req_dist[idx_2-1] + 1, right+1) 
            right = req_dist[idx_2]


        req_distance_list.append(req_dist)

    
    # summation and figuring out minimum idx 
    min_so_far = [0, math.inf]  # idx, best_distance 

    for block_idx in range(len(blocks)): 

        max_dist = 0  
        for req_idx in range(len(reqs)): 
            max_dist = max(max_dist, req_distance_list[req_idx][block_idx])

        if max_dist < min_so_far[1]: 
            min_so_far[1] = max_dist 
            min_so_far[0] = block_idx  


    for i in req_distance_list: 
        print(i)
    print(min_so_far)






blocks = [
    {
    "gym": False, 
    "school": True, 
    "store": False
    }, 
    {
    "gym": True, 
    "school": False, 
    "store": False
    }, 
    {
    "gym": True, 
    "school": True, 
    "store": False
    }, 
    {
    "gym": False, 
    "school": True, 
    "store": False
    }, 
    {
    "gym": False, 
    "school": True, 
    "store": True
    }, 
]

reqs = "gym school store".split() 
best_block_location(blocks, reqs)