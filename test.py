


blue = [3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32]
red =  [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1]


import math 

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    
    if len(redShirtSpeeds) != len(blueShirtSpeeds): 
        return 0 
    
    redShirtSpeeds.sort() 
    blueShirtSpeeds.sort() 
    size = len(redShirtSpeeds)
    
    best_sum = 0
    even = size%2 == 0 
    
    if fastest:  
        # reverse pairwise grouping 
        mid_idx  = size // 2 
        
        for idx in range(size):
            
            if even:  
                if (idx == mid_idx or idx == mid_idx - 1): 
                    to_add = max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
                
                # left half of array, add large redShirt 
                elif idx < mid_idx - 1: 
                    to_add = redShirtSpeeds[size-idx-1]
            
                # right half of array, add large blueShirt 
                else:
                    to_add = blueShirtSpeeds[idx]

            else:  
                if idx == mid_idx:  
                    to_add = max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
                    
                elif idx < mid_idx: 
                    to_add = redShirtSpeeds[size-idx-1]
            
                # right half of array, add large blueShirt 
                else:
                    to_add = blueShirtSpeeds[idx]                   
                
                
            best_sum += to_add 
                
    else:           
        for idx in range(size):
            best_sum += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
                    
    return best_sum


red.sort()
blue.sort() 
print(blue)
print(red)
print(tandemBicycle(red, blue, True))