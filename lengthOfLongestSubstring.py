









def lengthOfLongestSubstring(s): 

    longest_so_far = 0 
    seen = dict() 
    curr_cnt = 0 
    idx = 0 


    while idx < len(s): 

        char = s[idx]

        if char not in seen.keys(): 
            curr_cnt += 1 
            seen[char] = idx 
            idx += 1 

        else: 
            if longest_so_far < curr_cnt: 
                longest_so_far = curr_cnt

            idx = seen[char] + 1
            curr_cnt = 0 
            seen = dict()  

    if longest_so_far < curr_cnt: 
        longest_so_far = curr_cnt

    return longest_so_far



if __name__ == '__main__':
    
    s = "abc"
    print(lengthOfLongestSubstring(s)) 