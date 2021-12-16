

def steps(n): 

    num_ways_two = n // 2 
    num_ways_one = n % 2 

    return num_ways_two * 2 + num_ways_one * 1   



r = steps(4)
print(r) 