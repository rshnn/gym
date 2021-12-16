


from collections import Counter 

def build_char_dict(s): 

    char_set = dict() 

    for char in s: 
        if char in char_set.keys(): 
            char_set[char] += 1   
        else: 
            char_set[char] = 1

    return char_set 


def checkInclusion(s1, s2): 

    s1_dict = Counter(s1)


    w_size = len(s1) 
    left = 0 
    right = w_size  

    while right <= len(s2): 
        
        # right is non-inclusive in the slice 
        window = s2[left:right] 

        window_char_dict = Counter(window) 

        if s1_dict == window_char_dict: 
            return True 


        left += 1
        right += 1 


    return False 


if __name__ == '__main__':
    
    s1 = "hello"
    s2 = "ooolleoooleh"

    print(checkInclusion(s1, s2)) 