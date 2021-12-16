

def minimumWaitingTime(queries):
    # Write your code here.
    
    queries.sort() 
    n = len(queries)
    total_time = 0 

    for idx, q in enumerate(queries[:n-1]): 

        total_time += q * (n - idx - 1)

    return total_time  




if __name__ == '__main__':
    queries = [100, 100]
    expected = 17
    actual = minimumWaitingTime(queries)

    print(actual) 
