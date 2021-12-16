
alphabet = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

idx_lookup = {} 
for idx, char_set in enumerate(alphabet): 
    idx_lookup[idx+2] = list(char_set) 



from collections import deque 

def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    
    results = list() 
    stack = deque() 
    stack.append(("", 0))

    while stack: 

        substring, idx = stack.pop()  


        # stop condition 
        if idx == len(phoneNumber): 
            results.append(substring) 
            continue 

        num = int(phoneNumber[idx]) 
        next_state_substrings = list() 

        if num == 0 or num == 1: 
            next_state_substrings.append(substring + str(num))  
        else: 
            to_add = [substring + new_char for new_char in idx_lookup[int(num)]]
            for item in to_add: 
                next_state_substrings.append(item) 


        for s in next_state_substrings: 
            stack.append((s, idx+1))  
        


    return results 


results = list()

def recursive(array, idx, substring): 

    if idx == len(array): 
        print("adding ", substring)
        results.append(substring)  

    else: 
        num = array[idx]
        if num == '0' or num == '1': 
            recursive(array, idx+1, substring+num)  
            
        else: 
            next_chars = idx_lookup[int(num)]
            for char in next_chars: 
                recursive(array, idx+1, substring+char) 
            
    return




number = "22"

# print(phoneNumberMnemonics(number)) 
recursive(number, 0, "") 
print(results)