




def num_permutes(big_str, smol_str): 

    # build hash table 
    char_library = {}
    result_counter = 0 

    for char in smol_str: 
        if char in char_library.keys(): 
            char_library[char] += 1 
        else: 
            char_library[char] = 1 

    # iterate through bigstr with window technique 
    left = 0 
    right = 0 

    while left <= len(big_str) - len(smol_str): 

        if big_str[left] in char_library.keys(): 

            # starting a window 
            success = False 
            tmp_lib = char_library.copy() 
            tmp_lib[big_str[left]] -= 1 
            right = left 

            if len(smol_str) == 1: 
                success = True 


            for idx in range(1, len(smol_str)):
                curr = big_str[left+idx] 

                if curr not in tmp_lib.keys(): 
                    # failed window 
                    break 

                if tmp_lib[curr] == 0: 
                    # failed window 
                    break 

                else:
                    # success case  
                    # decrement count and continue with window 
                    tmp_lib[curr] -= 1  

                    if idx == len(smol_str) - 1: 
                        #last iter 
                        success = True 


            # for loop completes == success case.  add tally 
            if success: 
                result_counter += 1 

            del tmp_lib
        
        else: 
            # no match on current character.  move onto next in left 
            pass 

        left += 1 

    return result_counter  



big_str = "cbabcacabca" 
smol_str = "a"

print(num_permutes(big_str, smol_str))




from collections import Counter 

print(Counter(smol_str))