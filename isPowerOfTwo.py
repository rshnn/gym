


def hammingWeight(n): 

    return n & n-1

            

if __name__ == "__main__":

    n = bin('00000000000000000000000000001011')
    print(hammingWeight(n))
