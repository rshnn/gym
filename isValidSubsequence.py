



def isValidSubsequence(array, sequence):
    # Write your code here.
    
    p2 = 0 

    for i in range(len(array)): 

        if sequence[p2] == array[i]: 
            p2 += 1 

        if p2 == len(sequence): 
            return True 

    return False 





arr = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(isValidSubsequence(arr, sequence)) 