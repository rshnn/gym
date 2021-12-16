

from collections import deque 


def is_valid(i, j, mat): 

    I = len(mat) 
    J = len(mat[0])

    if (0 <= i < I) and (0 <= j < J): 
        return True 
    else: 
        return False 


def valid_neighbors(i, j, mat): 

    candidates = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    neighbors = list() 

    for cand in candidates: 
        if is_valid(cand[0], cand[1], mat): 
            neighbors.append(cand) 

    return neighbors 




def updateMatrix(mat): 
    """ Running BFS on each array item (for 2x) 
        Returning distance to first 0 
    """

    n, m = len(mat), len(mat[0])

    zero_locations = list() 

    for i in range(n): 
        for j in range(m): 

            if mat[i][j] == 0: 
                zero_locations.append((i, j))

            else: 
                mat[i][j] = None 


    for zero_loc in zero_locations: 

        i, j = zero_loc 
        fill_in_dists(i, j, mat)


    return mat   


def fill_in_dists(i, j, mat): 
    
    q = deque() 
    q.append((1, i, j))


    while q: 
        level, i, j = q.popleft()

        neighbors = valid_neighbors(i, j, mat)
        for neigh in neighbors: 
            if (mat[neigh[0]][neigh[1]] == None) or (mat[neigh[0]][neigh[1]] > level): 
                mat[neigh[0]][neigh[1]] = level 

                q.append((level+1, neigh[0], neigh[1]))

    return 

    

if __name__ == "__main__":

    mat = [[0,0,0],[0,1,0],[1,1,1]]

    out = updateMatrix(mat)

    print(out)
    # assert out == [[0,0,0],[0,1,0],[1,2,1]]


