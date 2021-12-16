"""
Returns rivers sizes in list.  River is 1.  Cardinally adjacent is valid.  
Diagonal is not 


Plan: 
- Travel through matrix as graph.  
    - each position has up to 4 neighbors.

"""

from collections import deque  

class Node(): 

    def __init__(self, val, neighbors=None): 
        self.val = val 
        
        if not neighbors: 
            self.neighbors = list()
        else: 
            self.neighbors = neighbors  


def _valid_neighbors(i, j, matrix): 
    """ returns list of tuples of valid cardinal neighbors""" 
     
    l = len(matrix) 
    w = len(matrix[0])
    out = list() 

    neighbors = [(i, j+1), (i, j-1), (i+1, j) , (i-1, j)]

    for neigh in neighbors: 

        i_, j_ = neigh 
        # Return TRUE is within grid   
        if (0 <= i_ < l) and (0 <= j_ < w):
            out.append(neigh) 

    return out 




def _travel_river(i, j, matrix): 

    # visit root 
    matrix[i][j] = 2 
    count = 1 

    fringe = deque() 

    neighbors = _valid_neighbors(i, j, matrix)
    for item in neighbors: 
        fringe.append(item)


    while fringe: 

        node = fringe.pop() 

        if matrix[node[0]][node[1]] == 1: 
            matrix[node[0]][node[1]] = 2 
            count += 1 

            neighbors = _valid_neighbors(node[0], node[1], matrix)
            for item in neighbors: 
                fringe.append(item)

        else: 
            continue 

    return count 



def riverSizes(matrix): 

    counts = list() 

    for i in range(len(matrix)): 
        for j in range(len(matrix[i])): 

            # travel along river and store count
            #  function will mutate matrix  

            if matrix[i][j] == 1: 
                count = _travel_river(i, j, matrix)
                counts.append(count)

    return counts 







if __name__ == '__main__':
    
    matrix = [
        [1, 0, 0, 1, 0], 
        [1, 0, 1, 0, 0], 
        [0, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1], 
        [1, 0, 1, 1, 0], 
    ]

    print(riverSizes(matrix))

    l = [1, 2, 3, 4]
    print(l.pop())
    print(l)
